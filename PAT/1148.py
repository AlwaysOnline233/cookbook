# Werewolf - Simple Version
'''
使用两个循环遍历每一种情况，判断该种情况下，是不是存在一个狼人撒谎以及一位村民撒谎。
如果是，则输出，因为这是按照顺序进行循环，所以一定是最小的解。如果到最后main函数都没有返回值，则输出一个No Solution。
如果狼人发言指定狼人是村民或者指定村民是狼人，则count_wof递增1.如果村民发言指定狼人是村民或者村民是狼人则count_lie递增1.
判断检验完所有人的发言后，撒谎的村民和撒谎的狼人是不是都是只有1人。如果是，输出答案.
'''


def main():
    n = int(input())
    get = []
    for x in range(n):
        get.append(int(input()))
    for i in range(n):
        for j in range(i+1, n):
            count_wof, count_lie = 0, 0
            for k in range(n):
                if k == i or k == j:
                    if get[k] > 0:
                        if get[k]-1 == i or get[k] - 1 == j:
                            count_wof += 1
                    else:
                        if abs(get[k])-1 != i and abs(get[k])-1 != j:
                            count_wof += 1
                else:
                    if get[k] >0:
                        if get[k] -1 ==i or get[k] -1 ==j:
                            count_lie += 1
                    else:
                        if abs(get[k])-1 != i and abs(get[k])-1 != j:
                            count_lie += 1
            if count_wof == 1 and count_lie == 1:
                print(i+1, j+1)
                return
    print("No Solution")


if __name__ == "__main__":
    main()
