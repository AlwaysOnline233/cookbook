# 映射名称到序列元素（通过名称访问元素）   collections.namedtuple()

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print('——————————————————————')
print('namedtuple的实例支持所有的普通元组操作')
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

