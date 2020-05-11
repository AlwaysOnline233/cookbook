# 字典运算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# zip()函数将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

print('——————————————————————————')
# 用zip()和orted()来排列字典数据   attention:zip()创建的是只能访问一次的迭代器
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print('——————————————————————————')
# 对比
print(min(prices))            # 仅作用于键
print(max(prices))
print('——————cf———————')
print(min(prices.values()))   # 仅作用于值
print(max(prices.values()))
print('——————cf———————')
print(min(prices, key=lambda k:prices[k]))   # 获取最小值最大值对应的键信息
print(max(prices, key=lambda k:prices[k]))
print('——————cf———————')
print(prices[min(prices, key=lambda k:prices[k])])
print(prices[max(prices, key=lambda k:prices[k])])