# 腌制：将数据对象保存到一个持久存储中的过程
# 解除腌制：从持久存储中恢复一个已保存的数据对象的过程
# pickle模块
# dump保存 load恢复

import pickle

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

try:                         # wb 访问模式改为 可写二进制模式
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)

except IOError as err:
    print('File error:' + str(err))

except pickle.PickleError as perr:
    print('Pickling Error:'+str(perr))