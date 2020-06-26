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

print('——————————————————————')
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

x = compute_cost([('xacker',0.2,80)])
print(x)
print('———————————————————————————————')
print('_replace()方法，它会创建一个全新的命名元组并将对应的字段用新的值取代')
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
print(s)

print('———————————————————————————————')
print('当命名元组拥有可选或者缺失字段时候，_replace()是一个方便的填充数据d的方法')
print('先创建一个包含缺省值的原型元组，然后使用 _replace()创建新的值被更新过的实例')
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
x = dict_to_stock(a)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
y = dict_to_stock(b)
print(x)
print(y)