# 匿名函数捕获变量值
# 用lambda定义了一个匿名函数，并想在定义时捕获到某些变量的值

# lambda表达式中的x是一个自由变量， 在运行时绑定值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))      # 30
print(b(10))      # 30

x = 15
print(a(10))      # 25
x = 3
print(a(10))      # 13


# 让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))      # 20
print(b(10))      # 30


print('——————————————————————————————')
# 通过在一个循环或列表推导中创建一个lambda表达式列表，并期望函数能在定义时就记住每次的迭代值
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))

print('——————————————————————————————')
# 不恰当的使用lambda表达式
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))
