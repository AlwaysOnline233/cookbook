# 函数转换为模块

'''这是nester.py模块'''


def print_lol(the_list):
    '''
    这个函数取一个位置参数"the_list"，这可以是任何python列表（包含嵌套列表的列表）。
    所指定的列表中的每个数据项会（递归地）输出到屏幕上，各数据项各占一行。
    :param the_list:
    :return:
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


