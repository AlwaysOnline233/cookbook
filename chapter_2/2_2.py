# 字符串开头或结尾匹配   str.startswith()  str.endswith()

import os
import re


filename = 'spam.txt'
t = filename.endswith('.txt')
print(t)
f = filename.startswith('file:')
print(f)

url = 'http://www.python.org'
u = url.startswith('http:')
print(u)


print('——————————example————————————————')
print('检查多种匹配可能')
# 将所有的匹配项放入到一个元组中去，然后传给 startswith() 或者 endswith()
filenames = os.listdir('.')
print(filenames)
p = [name for name in filenames if name.endswith(('.py', '.h')) ]
print(p)
y = any(name.endswith('.py') for name in filenames)
print(y)
# 当和其他操作比如普通数据聚合相结合的时候 startswith() 和 endswith() 方法是很不错的


print('——————————example————————————————')
# 必须要输入一个元组作为参数. list或set类型的选择项，确保传递参数前先调用tuple()将其转换为元组类型
choices = tuple(['http:', 'ftp:'])
url = 'http://www.python.org'
print(url.startswith(choices))


print('—————————————————————————————————')
print('切片实现：')
filename = 'spam.txt'
a = filename[-4:] == '.txt'
print(a)
url = 'http://www.python.org'
b = url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
print(b)


print('—————————————————————————————————')
print('正则表达式实现：')
url = 'http://www.python.org'
c = re.match('http:|https:|ftp:', url)
print(c)