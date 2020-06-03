# 内联回调函数
# 使用生成器和协程可以使得回调函数内联在某个函数中

from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


# Async 类
class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


# inlined_async 装饰器
def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))             # 使用 yield 语句内联回调步骤
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


test()



