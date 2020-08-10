# Raffle for Weibo Followers
'''
在输入的时候进行判断，如果当前元素是中奖者，且不再中奖者的名单中（即不是重复中奖），
则重置下一个中奖者的索引。如果是重复中奖者，则将下一个中奖者的索引加一递增
'''


def main():
    line = input().split(" ")
    m, n, s = int(line[0]), int(line[1]), int(line[2])
    followers = []
    for x in range(m):
        line = input()
        if x == s - 1:
            if line not in followers:
                followers.append(line)
                s = s + n
            else:
                s += 1
    if len(followers) > 0:
        for x in followers:
            print(x)
    else:
        print("Keep going...")


if __name__ == '__main__':
    main()