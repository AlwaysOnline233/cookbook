# 实现一个优先级队列
# 用heapq模块实现一个简单的优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):          # heapq.heappush()插入第一个元素
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1    # heappop（）总是返回"最小元素"  优先级为负使元素按从高到低排序

    def pop(self):
        return heapq.heappop(self._queue)[-1]   # heapq.heappop删除第一个元素


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())     # Item('bar')
print(q.pop())     # Item('spam')
print(q.pop())     # Item('foo')
print(q.pop())     # Item('grok')   foo和grok有相同的优先级，pop操作按照它们被插入到队列的顺序返回

print('——————————————————————————————')
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)
# 如果前两个比较已经可以确定结果，后面的比较操作不会发生
