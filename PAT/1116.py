# Come on! Let's C
'''
排名第一输出 Mystery Award，排名为质数输出 Minion，其他输出 chocolate。
如果查询的人之前被查过输出 Checked。
'''
import math


def prime(num):
    if num == 2:
        return True
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    dic = {}
    for x in range(n):
        line = input()
        dic[line] = x + 1
    k = int(input())
    for x in range(k):
        line = input()
        try:
            if dic[line] > 0:
                if dic[line] == 1:
                    print("{}: ".format(line)+"Mystery Award")
                elif prime(dic[line]):
                    print("{}: ".format(line)+"Minion")
                else:
                    print("{}: ".format(line)+"Chocolate")
            else:
                print("{}: ".format(line)+"Checked")
            dic[line] = -1
        except(KeyError):
            print("{}: ".format(line)+"Are you kidding?")