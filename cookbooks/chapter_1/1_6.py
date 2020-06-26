# 字典中的键映射多个值  multidict

'''
d = {
    'a': [1, 2, 3],    # 列表(保持元素插入顺序)
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},    # 集合(不关心元素顺序，去掉重复元素)
    'b': {4, 5}
}
'''

from collections import defaultdict

# 使用collections模块中的defaultdic来构造多值字典  自动初始化每个key刚开始对应的值
print('——————————————————————————————')
# defaultdic自动为将要访问的键(就算目前字典中不存在这样的键)创建映射实体
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print(d)
print(e)

print('——————————————————————————————')
# setdefault()用于普通字典的多值映射
z = {}
z.setdefault('a', []).append(1)
z.setdefault('a', []).append(2)
z.setdefault('b', []).append(4)
print(z)

