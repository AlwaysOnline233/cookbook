# 计算小球反弹高度
'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

dis = []      # 距离
height = []   # 高度

hei = 100     # 初始100米
time = 10     # 反弹10次

for i in range(1, time+1):    # 反弹次数
    if i == 1:                # 第一次
        dis.append(hei)
    else:
        dis.append(2*hei)     # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    hei /= 2                  # 反弹一半
    height.append(hei)        # 存入数组

print('总高度：{0}'.format(sum(dis)))
print('第10次反弹高度：height={0}'.format(height[-1]))  # 数列取反【-1】，倒数第一个,顺数最后一个
print('总的反弹距离：tour={0}'.format(dis[:]))
print('10次反弹高度：height={0}'.format(height[:]))
