# 删除序列相同元素并保持顺序

# 元素为hashable类型
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


print('——————————————————————')
# 集合消除重复元素
print(set(a))


print('————————————————————————————')
#元素不可哈希,如dict类型
def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe1(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe1(a, key=lambda d: d['x'])))


