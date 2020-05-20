# 排序
# 原地排序：是指按照指定顺序排列数据，然后用排序后的数据替换原来的数据  sort()
# 复制排序：是指按照指定顺序排列数据，然后返回原数据的一个有序副本。原数据顺序依然保留，只是对一个副本排序  sorted()

print('————————原地排序——————————————')
data = [6, 3, 1, 2, 4, 5]
print(data)
data.sort()
print(data)

print('————————复制排序——————————————')
data = [6, 3, 1, 2, 4, 5]
print(data)
data2 = sorted(data)
print(data)
print(data2)


