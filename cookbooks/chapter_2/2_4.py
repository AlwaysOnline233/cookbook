# 字符串匹配和搜索

import re

print('——————————————————————————————')
print('1）调用基本字符串方法')
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

print('——————————————————————————————')
print('2）使用正则表达式和re模块')
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):       # match() 总是从字符串开始去匹配
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

print('——————————————————————————————')
print('将模式字符串预编译为模式对象,使用同一个模式去做多次匹配')
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

print('——————————————————————————————')
print('findall()方法,查找字符串任意部分的模式出现位置')    # findall()匹配任意部分的模式出现位置
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))                 # findall()会搜索文本并以列表形式返回所有的匹配

print('——————————————————————————————')
print('在定义正则式的时候，通常会利用括号去捕获分组,因为可以分别将每个组的内容提取出来')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
print(text)
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

print('——————————————————————————————')
for m in datepat.finditer(text):           # finditer()以迭代方式返回匹配
    print(m.groups())

print('——————————————————————————————')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')    # 精确匹配，确保正则表达式以$结尾
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

print('使用re模块进行匹配和搜索文本的核心步骤: 先使用re.compile()编译正则表达式字符串，然后使用match(),findall(),finditer()等方法')