# 统计字符串里的字符数量
'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
'''

letter = 0
space = 0
digital = 0
other = 0
str = input('输入字符：')
for s in str:
    if s.isalpha():
        letter += 1
    elif s.isspace():
        space += 1
    elif s.isdigit():
        digital += 1
    else:
        other += 1
print('字母有:{}'.format(letter))
print('空格有:{}'.format(letter))
print('数字有:{}'.format(letter))
print('其它字符有:{}'.format(letter))