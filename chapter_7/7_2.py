# 只接受关键字参数的函数


# 将强制关键字参数放到某个*参数或者单个*后面
def recv(maxsize, *, block):
    # Receives a message
    pass
# print(recv(1024, True))           # TypeError
print(recv(1024, block=True))       # Ok


# 接受任意多个位置参数的函数中指定关键字参数
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))              # Returns -5
print(minimum(1, 5, 2, -5, 10, clip=0))      # Returns 0


# 使用强制关键字参数      recv()函数
msg = recv(1024, block=False)
print(msg)

print(help(recv))

