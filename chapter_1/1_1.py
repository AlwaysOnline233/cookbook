# 将序列分解为单独的变量

p = (4, 5)        # 赋多个值是不是不太方便？？
x, y = p
print(x)
print(y)


print('——————————————————————————————')
data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, share, price, data = data
# print(name)
# print(data)
name, share, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)


s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)
