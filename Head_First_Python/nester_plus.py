# 增加参数控制缩进


def print_lol(the_list, indent=False, level=0):
    '''

    :param the_list: 可以是任何python列表（包含嵌套列表的列表）
           level: 用来在遇到嵌套列表时插入制表符
           indent: 默认情况下不打开缩进特性
    :return:
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='')
            print(each_item)


names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]

print_lol(names)
print('——————————————————————————')
print_lol(names, True)
print('——————————————————————————')
print_lol(names, True, 2)
