# 字符串搜索和替换

import re
from calendar import month_abbr

print('——————————————————————————')
print('1)直接使用 str.replace()')
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

print('——————————————————————————')
print('2)使用re模块中的 sub() 函数')
'''
    re.sub(pattern, repl, string, count=0, flags=0)
        pattern : 正则中的模式字符串。
        repl : 替换的字符串，也可为一个函数。
        string : 要被查找替换的原始字符串。
        count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))   # 将形式为 11/27/2012 的日期字符串改成 2013-03-13

print('——————————————————————————')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')    # 打算用相同的模式做多次替换，考虑先编译提升性能
print(datepat.sub(r'\3-\1-\2', text))

print('——————————————————————————')
print('使用命名分组')
s = re.sub(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)', r'\g<year>-\g<month>-\g<day>', text)
print(s)

print('——————————————————————————')
def change_date(m):                        # 对于更加复杂的替换，可以传递一个替换回调函数来代替
    mon_name = month_abbr[int(m.group(1))]                         # 使用 group() 方法来提取特定的匹配部分。
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

date_time = datepat.sub(change_date, text)                   # 回调函数最后返回替换字符串
print(date_time)
print('一个替换回调函数的参数是一个match对象，也就是match()或find()返回的对象。')

print('使用 re.subn()可以知道有多少替换发生')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)