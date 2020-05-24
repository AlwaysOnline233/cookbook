# 字符串中插入变量

import sys
import string

# format()
print('————————————————————————————')
s = '{name} has {n} messages.'
ss = s.format(name='Guido', n=37)
print(ss)

print('————————————————————————————')
# 结合使用 format_map() 和 vars()
name = 'Guido'
n = 37
ss = s.format_map(vars())
print(ss)

print('————————————————————————————')
# vars() 也适用于对象实例
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
ss = s.format_map(vars(a))
print(ss)

print('————————————————————————————')
# attention:format 和 format_map() 并不能很好的处理变量缺失的情况
# s.format(name='Guido')    # KeyError: 'n'


# 一种避免这种错误的方法是另外定义一个含有 __missing__() 方法的字典对象
class safesub(dict):
    # 防止key找不到
    def __missing__(self, key):        # __missing__() 定义如何处理缺失的值
        return '{' + key + '}'


# 利用这个类包装输入后传递给 format_map()
del n # Make sure n is undefined
ss = s.format_map(safesub(vars()))     # SafeSub 被定义为对缺失的值返回一个占位符
print(ss)

print('————————————————————————————')
# 将变量替换步骤用一个工具函数封装起来
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
# f_locals 是一个复制调用函数的本地变量的字典,可以改变 f_locals 的内容，但是这个修改对于后面的变量访问没有任何影响

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

print('————————————————————————————')
# 使用字符串模版                           # format() 和 format_map() 更加先进，应优先选择
s = string.Template('$name has $n messages.')
ss = s.substitute(vars())
print(ss)