# 字符串对齐


# 基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center()
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.rjust(20, '='))
print(text.center(20))
print(text.center(20, '*'))

print('——————————————————————————————————')
# 函数 format() 同样可以用来对齐字符串
print(format(text, '>20'))
print(format(text, '=>20s'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '*^20s'))

print('——————————————————————————————————')
# 格式化多个值,这些格式代码也可以被用在 format() 方法中
print('{:>10s} {:>10s}'.format('Hello', 'World'))

print('——————————————————————————————————')
# format() 可以用来格式化任何值,如格式化数字
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f')) 