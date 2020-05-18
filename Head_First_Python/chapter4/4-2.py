# 异常作为一个标识符

man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!!!')

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file=man_file)
    print(other, file=other_file)

except IOError as err:                    # 为异常对象给定一个名称
    print('File error:' + str(err))       # str()把异常对象转换为字符串

finally:                           # 无论是否运行出错，finally组中代码总会运行
    # 调用close()前先查看文件名是否存在
    if 'man_file' in locals():     # local()返回当前作用域中定义的所有名的一个集合
        man_file.close()
    if 'other_file' in locals():
        other_file.close()
