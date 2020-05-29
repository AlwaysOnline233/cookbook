# 定义有默认参数的函数


# 给参数指定一个默认值
def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)


# 默认参数的值仅仅在函数定义的时候赋值一次
x = 42
def spam2(a, b=x):
    print(a, b)

spam2(1)        # 1 42
x = 23
spam2(1)        # 1 42      改变x的值的时候对默认参数值并没有影响


# 如果默认参数是一个可修改的容器如一个列表、集合或者字典，可以使用None作为默认值
def spam3(a, b=None):
    if b is None:
        b = []


# 如果不想提供一个默认值，而是想测试下某个默认参数是不是有传递进来
_no_value = object()           # 创建一个对象实例
def spam4(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

spam4(1)
spam4(1, 2)
spam4(1, None)