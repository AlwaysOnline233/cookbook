# 判断回文


def f(str):
    return str == str[::-1]


print(f('asdzxc'))
print(f('abcdcba'))


def f2(string):
    for i in range(len(string)):
        if string[i] != string[len(string) - i-1]:
            break
    else:
        return True

    return False


print(f2('1234321'))
print(f2('12343214'))