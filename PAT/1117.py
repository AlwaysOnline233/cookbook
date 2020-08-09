# Eddington Number
'''
从N向1遍历，长度为long。
使用列表推导式，计算这个整型串中大于long的有几个。如果大于等于long个，则输出long。
如果没有输出，则只可能是0个
'''


def main():
    n = int(input())
    line = input().split(' ')
    num = [int(x) for x in line]
    flag = 0
    for x in range(n):
        long = n - x
        if len([x for x in num if x > long]) >= long:
            print(long)
            flag = 1
            break
    if flag == 0:
        print(0)


if __name__ == '__main__':
    main()