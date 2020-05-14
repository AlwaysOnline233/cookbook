# 转换并同时计算数据
import os

# 使用生成器表达式参数
nums = [1, 2, 3, 4, 5]
# s = sum((x * x for x in nums))    # 显式的传递一个生成器表达式对象
s = sum(x * x for x in nums)        # 省略了括号
print(s)

print('—————————————example—————————————————')
# Determine if any .py files exist in a directory
files = os.listdir('../chapter_1')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

