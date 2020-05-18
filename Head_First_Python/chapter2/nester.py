# 函数转换为模块

'''这是nester.py模块'''


def print_lol(the_list, level=0):
    '''
    这个函数取一个位置参数"the_list"，这可以是任何python列表（包含嵌套列表的列表）。
    所指定的列表中的每个数据项会（递归地）输出到屏幕上，各数据项各占一行。
    :param the_list: 列表
           level: 用来在遇到嵌套列表时插入制表符
    :return:
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print('\t', end='')
            print(each_item)

