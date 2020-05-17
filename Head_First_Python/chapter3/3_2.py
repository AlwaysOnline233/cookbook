# 处理异常：1）增加额外的代码和逻辑

import os

if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    print('——————————————————————————————')
    for each_line in data:
        if not each_line.find(':') == -1:     # find()找到子串返回该子串在原字符串中索引位置，未找到返回-1
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print('said:', end='')
            print(line_spoken, end='')

    data.close()
else:
    print('The data file is missing!!!')