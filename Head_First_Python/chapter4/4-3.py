# 用with处理文件
# with语句利用了一种名为上下文管理协议的python技术

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
    with open('man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_data.txt', 'w') as other_file:
        print(other, file=other_file)

except IOError as err:                    # 为异常对象给定一个名称
    print('File error:' + str(err))       # str()把异常对象转换为字符串


