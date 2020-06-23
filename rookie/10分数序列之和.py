# 分数序列之和
'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
分析：前一项的分子是当前项的分母，前一项的分子分母之和是当前项的分子
'''

front = 2
down = 1
sum = 0

for i in range(20):
    sum += front/down
    t = front
    front = front + down
    down = t

print(sum)
