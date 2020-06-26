# 查找两字典的相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())     # Find keys in common
print(a.keys() - b.keys())     # Find keys in a that are not in b
print(a.items() & b.items())   # Find (key,value) pairs in common

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
print('字典的keys()返回一个展现键集合的键视图对象，可以直接使用键视图对象执行一些普通的集合操作，如集合并、交、差运算')
print('字典的items()返回一个包含(键，值)对的元素视图对象,也支持集合操作，并且可以被用来查找两个字典有哪些相同的键值对')
print('字典的values()也类似,但是它并不支持这里的集合操作,(可以先将值集合转换成set,然后再执行集合运算)')