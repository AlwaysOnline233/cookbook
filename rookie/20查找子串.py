# 查找子串

# str.find(str, beg=0, end=len(string))
str1 = "this is string example....wow!!!"
str2 = "exam"

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))


print('——————————————————————')
string = "I love python"
sub = 'pyth'

def find(string, sub):
    index = -1
    for i in range(len(string)):
        if string[i] == sub[0]:
            m = i
            n = 0
            while m < len(string) and n < len(sub) and string[m] == sub[n]:
                m += 1
                n += 1
            if n == len(sub):
                index = i
                break
    return index

print(find(string, sub))
