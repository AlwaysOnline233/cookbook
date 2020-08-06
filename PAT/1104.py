# Sum of Number Segments
'''
考虑（0.1 0.2 0.3 0.4 0.5）这个示例，0.1会在子串中出现0+5次，0.2会在子串中出现4*1+4次，
0.3会在子串中出现3*2+3次，0.4会在子串中出现2*3+2次，0.5会出现1*5+0次
'''


def main():
    n = int(input())
    line = input().split(" ")
    num = [float(x) for x in line]
    s = 0
    for i in range(n):
        s += num[i] * (n-i) * (i+1)
    print('{:.2f}'.format(s))


if __name__ == "__main__":
    main()