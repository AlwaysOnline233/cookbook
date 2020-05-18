# 删除字符串中不需要的字符

import re

# 默认情况下，这些方法会去除空白字符
s = ' hello world \n'
print(s.strip())           # strip() 能用于删除开始或结尾的字符
print(s.lstrip())          # lstrip() 从左执行删除操作
print(s.rstrip())          # rstrip() 从右执行删除操作

print('——————————————————————')
# 指定删除字符
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

print('——————————————————————')
# 去除操作不会对字符串的中间的文本产生任何影响
s = ' hello     world \n'
s = s.strip()
print(s)

print('——————————————————————')
# 使用 replace() 或用正则表达式替换中间空格
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))

print('——————————————————————')
# 将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取多行数据
filename = '../chapter_1/somefile.txt'
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)