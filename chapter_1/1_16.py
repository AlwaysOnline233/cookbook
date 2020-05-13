# 过滤序列元素

from itertools import compress

# 使用列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
less = [n for n in mylist if n > 0]
more = [n for n in mylist if n < 0]
print(less)
print(more)

print('————————————————————————————')
# 使用生成器表达式迭代产生过滤的元素
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

print('————————————————————————————')
# 过滤规则复杂，使用内建的filter()函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
print('filter()函数创建了一个迭代器，如果想得到一个列表，就得使用list()去转换')

print('————————————————————————————')
# 将不符合条件的值用新的值代替
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

print('————————————————————————————')
# itertools.compress()  适用另外一个相关联的序列来过滤某个序列
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]      # 将对应count值大于5的地址全部输出
print(more5)
print(list(compress(addresses, more5)))
print('关键点在于先创建一个Boolean序列，指示哪些元素符合条件。然后compress()根据这个序列去选择输出对应位置为True的元素')
print('和filter()类似,compress()也是返回的一个迭代器。因此，如果需要得到一个列表，需要使用list()来将结果转换为列表类型')