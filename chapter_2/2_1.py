# 使用多个界定符分割字符串    re.split()
# split()只适用于简单的字符串分割
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'      # 两个字符以上切割需要放在 [ ] 中
print(re.split(r'[;,\s]\s*', line))           # \s 匹配任意非空白字符，如空格、制表符、换页符等 [^\t\n\r\f\v]

print('使用括号捕获分组，被匹配的文本也将出现在结果列表中')
fields = re.split(r'(;|,|\s)\s*', line)       # 使用括号捕获分组，默认保留分割符
print(fields)

print('————————————————————————————')
print('获取分割字符')
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

print('————————————————————————————')
print('用前面的分割字符串重新构造一个新的输出字符串')
# Reform the line using the same delimiters
s = ''.join(v+d for v, d in zip(values, delimiters))
print(s)

print('————————————————————————————')
print('使用括号来分组正则表达式,不保留分割字符串到结果列表')
x = re.split(r'(?:,|;|\s)\s*', line)                # 不保留分隔符 形如 (?:...)
print(x)