# N Queens Puzzle
'''
使用get数组存储每一个皇后放置的行数，然后对于每一个（除了第一个）皇后进行检验，
是否同一行有皇后(get[i] == get[j])是否斜对角有皇后(abs(i – j) == abs(get[i] – get[j]))。
如果都没有则符合要求，进行输出。
'''


def main():
    num = int(input())
    for x in range(num):
        line = input().split(" ")
        flag = 0
        get = [int(x)-1 for x in line[1:]]
        n = int(line[0])
        for i in range(n):
            if i != 0 and flag == 0:
                for j in range(i):
                    if abs(i - j) == abs(get[i] - get[j]) or get[i] == get[j]:
                        flag = 1
                        break
            elif i != 0:
                break
        if flag == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()