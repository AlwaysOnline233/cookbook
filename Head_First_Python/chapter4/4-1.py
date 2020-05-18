# 持久存储  数据保存到文件

'''
  w: 打开指定的文件来完成写。若该文件已经存在，则会清空它现有的内容
  a: 追加到一个文件
  w+: 打开一个文件完成读和写（不清除）
  若打开一个文件完成写，但这个文件不存在，首先会创建这个文件，然后再打开文件进行写
'''

# 将数据存到磁盘文件中
# 将磁盘文件分别命名为man_data.txt和other_data.txt，分别存储一个人讲话和另一个人讲话
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

except IOError:
    print('File error.')

finally:                           # 无论是否运行出错，finally组中代码总会运行
    # 调用close()前先查看文件名是否存在
    if 'man_file' in locals():     # local()返回当前作用域中定义的所有名的一个集合
        man_file.close()
    if 'other_file' in locals():
        other_file.close()




