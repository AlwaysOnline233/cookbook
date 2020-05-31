# 减少可调用对象的参数个数

from functools import partial
import math
import logging
from multiprocessing import Pool


# 减少某个函数的参数个数 functools.partial()  允许给一个或多个参数设置固定的值
def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)     # a=1
s1(2, 3, 4)               # 1 2 3 4
s1(4, 5, 6)               # 1 4 5 6

s2 = partial(spam, d=42)  # d = 42
s2(1, 2, 3)               # 1 2 3 42
s2(4, 5, 5)               # 4 5 5 42

s3 = partial(spam, 1, 2, d=42)    # a = 1, b = 2, d = 42
s3(3)                             # 1 2 3 42
s3(4)                             # 1 2 4 42
s3(5)                             # 1 2 5 42


# 有一个点的列表来表示(x,y)坐标元组
points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

'''
假设想以某个点为基点，根据点和基点之间的距离来排序所有的这些点。 
sort() 接受一个关键字参数来自定义排序逻辑，但它只接受一个单个参数的函数(distance()很明显是不符合条件的)。 
现在我们可以通过使用 partial() 来解决这个问题
'''
pt = (4, 3)
points.sort(key=partial(distance,pt))
print(points)


# partial() 被用来微调其他库函数所使用的回调函数的参数
# 使用 multiprocessing 来异步计算一个结果值，这个值被传递给一个接受一个result值和一个可选logging参数的回调函数
def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


def add(x, y):
    return x + y


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
    # 当给 apply_async() 提供回调函数时，通过使用 partial() 传递额外的 logging 参数。
    # 而 multiprocessing 对这些一无所知,它仅仅只是使用单个值来调用回调函数
