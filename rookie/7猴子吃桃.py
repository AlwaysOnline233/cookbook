# 猴子吃桃
'''
猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个,第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''

# 循环算法
current = 1
for day in range(9, 0, -1):
    yesterday = (current+1)*2
    current = yesterday

print(yesterday)


# 递归算法
def f(n):
    if n == 1:
        return 1
    else:
        return (f(n-1)+1)*2


print(f(10))
