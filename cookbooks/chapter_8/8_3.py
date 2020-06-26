# 让对象支持上下文管理协议

# 让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


# 创建一个网络连接
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


# 连接的建立和关闭是使用 with 语句自动完成的
conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed

'''
编写上下文管理器的主要原理是代码会放到 with 语句块中执行。当出现 with 时，对象的 __enter__() 方法被触发， 
它返回的值(如果有)会被赋值给as声明的变量。然后，with 语句块里面的代码开始执行。最后，__exit__()被触发进行清理工作。
'''