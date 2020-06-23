# 递归打印
'''
使用递归函数从终端输入5个字符串，倒序输出
'''


def f(n):
    value = input('input str:\n')
    if n <= 1:
        print(value)
    else:
        f(n-1)
        print(value)

f(5)