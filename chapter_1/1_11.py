# 命名切片

# 从一个记录中的某些固定位置提取字段
records = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(records[SHARES]) * float(records[PRICE])
print(cost)

print('——————————————————————————')
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

# 调用切片的indices(size)映射到一个已知大小的序列上
print('——————————————————————————')
s = 'Helloworld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])