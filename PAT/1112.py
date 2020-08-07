# Stucked Keyboard
'''
先使用count，用bad字符串保存可能是卡住的键位。之后遍历bad字符串，
如果获取的字符串经过replace(x*num)操作后便没有这个字符了，那么这个字符就是卡住的，否则，这个字符是完好的
'''
# count()用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
# str.count(sub, start= 0,end=len(string))


def main():
    num = int(input())
    line = input()
    bad = ''
    for x in line:
        if line.count(x) % num == 0 and x not in bad:
            bad += x
    for x in bad:
        co = line
        co = co.replace(x*num, '')
        if co.count(x) != 0:
            bad = bad.replace(x, '')
    print(bad)
    for x in bad:
        line = line.replace(x*num, x)
    print(line)


if __name__ == '__main__':
    main()