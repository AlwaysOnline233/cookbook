# 处理异常：2）异常处理机制

'''split()传回一个列表。
   python中有2种类型列表：可以改变的列表（中括号包围）；一旦创建不可改变的列表（小括号包围）
   后者是不可改的列表 元组。可以认为元组是一个常量列表。
'''
try:
    data = open('sketch.txt')

    print('——————————————————————————————')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print('said:', end='')
            print(line_spoken, end='')
        except ValueError:              # 特定指定异常
            pass

    data.close()
except IOError:                         # 特定指定异常
    print('The data file is missing!!!')


