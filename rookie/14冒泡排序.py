# 冒泡排序法


def bubbleSort(lst):
    for i in range(len(lst)-1):           # 控制排序次数
        for j in range(len(lst)-1-i):     # 控制排序时的数据范围，已有序的区域不需要再排序
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


lst = [5, 8, 2, 4, 1, 9, 15]
print(bubbleSort(lst))
