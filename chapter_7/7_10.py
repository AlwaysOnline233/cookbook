# 带额外状态信息的回调函数


# 定义一个需要调用回调函数的函数
def apply_async(func, args, *, callback):
    result = func(*args)    # Compute the result
    callback(result)        # Invoke the callback with the result


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


# 回调函数的调用
apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)


# 回调函数访问外部信息
# 1) 使用一个绑定方法来代替一个简单函数
# 如保存一个内部序列号，每次接收到一个 result 的时候序列号加1
class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


# 创建一个类的实例，然后用它的 handler() 绑定方法来做为回调函数
r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)


# 2) 作为类的替代，可以使用一个闭包捕获状态值
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


# 使用闭包方式
handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)


# 3) 使用协程
def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler2()
next(handler)       # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)
