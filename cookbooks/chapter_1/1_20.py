# 合并多个字典或映射

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# 在两个字典中执行查找操作(如先从a中找，若找不到再在b中找)。使用collections模块中的ChainMap类
c = ChainMap(a, b)
print(c['x'])       # Outputs 1 (from a)
print(c['y'])       # Outputs 2 (from b)
print(c['z'])       # Outputs 3 (from a)
print('——————————————————————')
print(len(c))
print(list(c.keys()))
print(list(c.values()))  # 出现重复键，第一次出现的映射值会被返回c['z']总是会返回字典a中对应的值
print('对于字典的更新或删除操作总是影响的是列表中第一个字典')
c['z'] = 10
c['w'] = 40
del c['x']
# del c['y']      # KeyError: "Key not found in the first mapping: 'y'"
print(a)

print('——————————————————————————')
values = ChainMap()
values['x'] = 1
values = values.new_child()      # Add a new mapping
values['x'] = 2
values = values.new_child()      # Add a new mapping
values['x'] = 3
print(values)
print(values['x'])
values = values.parents          # Discard last mapping
print(values['x'])
values = values.parents          # Discard last mapping
print(values['x'])
print(values)

print('——————————————————————————')
# 作为 ChainMap 的替代，考虑使用 update() 方法将两个字典合并
merged = dict(b)
merged.update(a)
print(merged['y'])
print(merged['z'])
a['y'] = 13
print(merged['y'])     # 如果原字典做了更新，这种改变不会反应到新的合并字典中去