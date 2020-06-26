# 返回多个值的函数


# 为了能返回多个值，函数直接return一个元组
def myfun():
    return 1, 2, 3


# 调用返回一个元组的函数的时候，通常会将结果赋值给多个变量   即元组解包
a, b, c = myfun()
print(a)
print(b)
print(c)
# 返回结果也可以赋值给单个变量， 这时候这个变量值就是函数返回的那个元组本身
z = myfun()
print(z)


# myfun()看上去返回多个值，实际上是先创建了一个元组然后返回的。
# 实际上我们使用的是逗号来生成一个元组，而不是用括号
x = (1, 2)    # With parentheses
print(x)
y = 1, 2      # Without parentheses
print(y)
