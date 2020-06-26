# 保留最后N个元素
#
from collections import deque    # collections.deque保留有限历史记录


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines           # yield函数，生成器
        previous_lines.append(line)


# .表示为当前路径  ..表示为当前路径的父级目录
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# 使用deque(maxlen=N)构造函数会新建一个固定大小的队列，当新元素加入且这个队列已满，最老的元素自动被移除
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# 不设置最大队列大小，会得到无限大小队列
print('————————————————————————')
e = deque()
e.append(1)
e.append(2)
e.append(3)
print(e)
e.appendleft(4)
print(e)
e.pop()
print(e)
print(e.popleft())
