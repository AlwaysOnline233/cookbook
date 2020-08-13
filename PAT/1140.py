# Look-and-say Sequence
'''
使用递归的describe函数进行描述，当进入最后一次描述时，返回结果。
每次进行描述的时候，从0开始遍历整个字符串，遇到第一个不相同的字符时，完成前面的字符描述。
要注意遇上最后一个字符的时候，要进行描述并结束
'''


def describe(d, k):
    if k == 1:
        return d
    else:
        temp, start = '', 0
        for x in range(len(d)):
            if d[x] != d[start]:
                temp = temp + d[start] + str(x - start)
                start = x
            if x == len(d) -1:
                temp = temp + d[start] + str(x - start + 1)
        return describe(temp, k - 1)


if __name__ == "__main__":
    line = input().split(" ")
    result = describe(line[0], int(line[1]))
    print(result)
