# Chain the Ropes
'''
最先加进去的绳子要被折叠最多次，所以短的绳子应该比长的绳子早加入。
因此进行排序，每次加入的都是最小的绳子，最后使用int()向下取整就可以了。
'''


def main():
    n = int(input())
    line = input().split(' ')
    length = sorted([int(x) for x in line])
    s = length[0]
    for x in range(1, n):
        s = (s + length[x]) / 2
    print(int(s))


if __name__ == '__main__':
    main()