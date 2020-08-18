# Friend Numbers
'''
给定一串字符串，求互不相同的每个数字的各个位数之和。最后升序输出
使用循环，相加各位，将结果保存在集合中
'''


def main():
    n = int(input())
    line = input().split(' ')
    sums = set()
    for x in line:
        count = 0
        for i in x:
            count += int(i)
        sums.add(count)
    sums = sorted(sums)
    print(len(sums))
    output = [str(x) for x in sums]
    print(" ".join(output))


if __name__ == '__main__':
    main()
