# 定义匿名或内联函数  通过某个快捷方式以内联方式来创建sort()


def add(x, y):
    return x + y


# lambda来计算一个表达式的值
add = lambda x, y: x + y       # 与上面add()函数效果同
print(add(2, 3))
print(add('hello', 'world'))


# lambda来排序
names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
s = sorted(names, key=lambda name: name.split()[-1].lower())
print(s)





