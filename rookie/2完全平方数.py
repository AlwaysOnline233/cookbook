# 完全平方数
'''
打印10000以内的完全平方数
'''

import math


index = 1
num = 0

while num < 10000:
    num = index * index
    print(num)
    index += 1


'''
有这样的数，如果这个数加100是一个完全平方数，加268也是一个完全平方数，求10000以内所有符合这个要求的数值
'''
for i in range(10000):
    # 转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)
