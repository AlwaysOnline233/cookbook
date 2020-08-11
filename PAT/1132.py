# Cut Integer
'''
字符串切片，然后转换类型，进行求余。注意，如果A*B为0，会报错
'''


def main():
    n = int(input())
    for x in range(n):
        line = input()
        num = int(len(line)/2)
        a, b, c = int(line[:num]), int(line[num:]), int(line)
        if a*b == 0 or c % (a * b) != 0:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()