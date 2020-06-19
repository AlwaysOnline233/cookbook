# 求三位数组合
'''
已知有一个list，里面有4个数字，分别是3，6，2，7 ，这四个数字能组成多少个互不相同且无重复数字的三位数？
比如362算一个，326算一个，请逐个输出他们
分析：
三层嵌套循环，每一层循环从list中取出一个数字，这三个数字组成一个三位数
组成的三位数互不相同，且没有重复数字，这需要对取出来的三个数字进行去重
'''

lst = [3, 6, 2, 7]
number_lst = []

for i in lst:
    for j in lst:
        for k in lst:
            if i != j and i != k and j != k:
                # number_lst.append('{first}{second}{third}'.format(first=i,second=j,third=k))
                number_lst.append((i*100 + j*10 + k))


print('符合条件的数字有：')
print(len(number_lst))
for item in number_lst:
    print(item)

