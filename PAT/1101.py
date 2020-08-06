# Quick Sort
'''
用数组b保存sorted函数排序后的数组，循环遍历，
如果此时a中元素和b中元素相等，则考虑该元素是否大于a中该索引位置前的最大值，如果是，则加入输出数组
'''


def main():
    num = int(input())
    line = input().split(" ")
    a = [int(x) for x in line]
    b = sorted(a)
    result = []
    leftMax = -1
    n = 0
    for x in range(num):
        if a[x] is b[x]:
            if b[x] > leftMax:
                result.append(b[x])
                n += 1
        if a[x] > leftMax:
            leftMax = a[x]
    result = [str(x) for x in result]
    print(n)
    print(' '.join(result))


if __name__ == "__main__":
    main()