# 通过某个关键字排序一个字典列表   operator 模块的 itemgetter 函数

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

print('——————————————————————————————')
print('itemgetter() 函数也支持多个keys')
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

print('——————————————————————————————')
print('itemgetter() 有时候也可以用 lambda 表达式代替')
# rows_by_fname = sorted(rows, key=lambda r: r['fname'])
# rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

print('——————————————————————————————')
print('min() 和 max()也可以实现')
# min(rows, key=itemgetter('uid'))
# max(rows, key=itemgetter('uid'))