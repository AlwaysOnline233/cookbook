# 改变对象的字符串显示


# 重新定义它的 __str__() 和 __repr__() 方法
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # __repr__()返回一个实例的代码表示形式，通常用来重新构造这个实例。内置的 repr() 函数返回这个字符串
        return 'Pair({0.x!r}, {0.y!r})'.format(self)  # 格式化代码{0.x}对应的是第1个参数的x属性,0实际上指的就是self本身
        # return 'Pair(%r, %r)' % (self.x, self.y)    # 也可以使用 % 操作符

    def __str__(self):   # __str__()将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(p.__repr__())
print(p.__str__())
print(p)

print('p is {0!r}'.format(p))   # !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()
print('p is {0}'.format(p))
