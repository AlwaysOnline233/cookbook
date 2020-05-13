# 从字典中提取子集

# 构造一个字典，它是另外一个字典的子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print('使用字典推导')
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

print('————————————————————————')
print('创建一个元组序列然后传给dict()实现')
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)
p4 = {key: prices[key] for key in prices.keys() & tech_names}
print(p4)
