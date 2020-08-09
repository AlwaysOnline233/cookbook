# Eddington Number
'''

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