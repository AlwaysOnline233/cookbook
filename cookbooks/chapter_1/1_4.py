# 查找最大或最小的N个元素  nlargest()   nsmallest()

import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))     # [42, 37, 23]
print(heapq.nsmallest(2, nums))    # [-4, 1]
print('——————————————————————————')
heap = list(nums)    # 在底层实现，会先将集合数据进行堆排序后放入列表
heapq.heapify(heap)
print(heap)          # heap[0]永远是最小元素


print('——————————————————————————')
portfolio = [
    {'name':'IBM', 'share':100, 'price':91.1},
    {'name':'AAPL', 'share':50, 'price':543.22},
    {'name':'FB', 'share':200, 'price':21.09},
    {'name':'HPQ', 'share':35, 'price':31.75},
    {'name':'YHOO', 'share':45, 'price':16.35},
    {'name':'ACME', 'share':75, 'price':115.65},
]
#  lambda 来创建匿名函数
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])  # 以price的值进行比较
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)


print('——————————————————————————')
print('当要查找的元素个数相对较小，函数nlargest()和nsmallest()是合适的。若仅想查找唯一的最小或最大(N=1)的元素,那么min()和max()函数更快些')
print('类似的，如果N的大小和集合大小接近，通常先排序集合然后再使用切片操作(sorted(items)[:N] 或者是 sorted(items)[-N:])')
print('需要在正确场合使用函数nlargest()和nsmallest()才能发挥它们的优势（如果N快接近集合大小了，那么使用排序操作会更好些）')