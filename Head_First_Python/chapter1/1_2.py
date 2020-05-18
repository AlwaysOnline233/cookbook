# 在列表中存储列表
movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
          ['Graham Chapman',
            ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
print(movies[4][1][3])       # output  Eric Idle

for each_item in movies:
    print(each_item)        # for循环只能打印外列表的各个数据项，嵌套在内列表中的下一层内列表原样打印


print('————————————————————————————————')
# isinstance() 检查某个标识符是否包含某个特定类型的数据
names = ['Michael', 'Terry']
isinstance(names, list)          # 询问names是否是一个列表
num_names = len(names)
isinstance(num_names, list)


print('————————————————————————————————')
# 列表中查找列表
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)


print('————————————————————————————————')
# 创建函数，不要重复代码
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print(print_lol(movies))
