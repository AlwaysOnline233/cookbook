# 字典排序
# collections模块中的OrderedDict类控制字典中的元素顺序  保持元素被插入的顺序

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])

# OrderedDict构建需要序列化或编码成其他格式的映射
# 如控制以JSON编码后的字段的顺序
print('————————————————————————')
print(json.dumps(d))

print('————————————————————————')
print('OrderedDict内部维护着一个根据键插入顺序排序的双向链表。')
print('每当一个新元素插入进来，它会被放到链表尾部。对于一个已经存在的键的重复赋值不会改变键的顺序')
print('attention:一个OrderedDict的大小是一个普通字典的两倍，因为它内部维护着另外一个链表')
print('要构建一个需要大量OrderedDict实例的数据结构的时候,得权衡一下是否使用OrderedDict')