# Integer Set Partition
'''
项数差只能取值0或1，这取决与N是奇数还是偶数。而和的差则是两个集合的和差。
按照升序排列整型串，前半部分为A1，后半部分为A2。求A2与A1的和差即可。
因为如果有交集元素，两个集合都会去除使得项数差最小。所以去不去都一样，直接使用sum函数求和然后相减即可
'''


def main():
    n = int(input())
    line = input().split(' ')
    num = [int(x) for x in line]
    num = sorted(num)
    a1 = num[0: n//2]
    a2 = num[n//2: n]
    print(n % 2, sum(a2)-sum(a1))


if __name__ == '__main__':
    main()