# 文件

import os


print(os.getcwd())              # 当前的工作目录
data = open('sketch.txt')       # 打开命名文件
print(data.readline(), end='')  # 从文件获取一个数据行
print(data.readline(), end='')
print('————————————')
data.seek(0)                    # 回到文件起始位置
for each_line in data:
    print(each_line, end='')    # 迭代，获取每个数据行

data.close()                   # 关闭文件



