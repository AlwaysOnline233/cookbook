# Finding Average
'''
使用legal和illegal两个数组存储数字。接受输入完成之后，
先遍历illegal数组，输出所有非法数字的错误提示，最后根据条件输出平均值信息
'''


def main():
    num = int(input())
    line = input().split(" ")
    legal, illegal = [], []
    for x in line:
        try:
            if -1000 <= float(x) <= 1000:
                if '.' in x:
                    if len(x) - x.find('.')-1 <= 2:
                        legal.append(float(x))
                    else:
                        illegal.append(x)
                else:
                    legal.append(float(x))
            else:
                illegal.append(x)
        except:
            illegal.append(x)
    for x in illegal:
        output = 'ERROR: {} is not a legal number'.format(x)
        print(output)
    if len(legal) == 0:
        output = 'The average of 0 numbers is Undefined'
    elif len(legal) == 1:
        ave = sum(legal) / len(legal)
        output = 'The average of {} number is {:.2f}'.format(len(legal), ave)
    else:
        ave = sum(legal) / len(legal)
        output = 'The average of {} numbers is {:.2f}'.format(len(legal), ave)
    print(output)


if __name__ == '__main__':
    main()
