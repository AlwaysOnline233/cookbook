# A Delayed Palindrome
'''
在while循环内将字符串倒置，转换类型相加。
设置flag变量判断是否输出了，使用check函数判断是否是回文数
'''


def check(string):
    num = len(string)
    for x in range(num // 2):
        if string[x] != string[num-1-x]:
            return False
    return True


if __name__ == "__main__":
    num = int(input())
    n = 10
    flag = 0
    while(n > 0):
        if check(str(num)):
            print('{} is a palindromic number.'.format(num))
            flag = 1
            break
        else:
            a = str(num)[::-1]
            temp = num + int(a)
            print(num, '+', a, '=', temp)
            num = temp
        n -= 1
    if flag == 0:
        print('Not found in 10 iterations.')