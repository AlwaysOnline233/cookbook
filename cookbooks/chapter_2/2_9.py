# 将Unicode文本标准化

import unicodedata
print('————————————————————————————')
# 这里的文本”Spicy Jalapeño”使用了两种形式来表示。
# 第一种使用整体字符”ñ”(U+00F1)，第二种使用拉丁字母”n”后面跟一个”~”的组合字符(U+0303)
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

print('————————————————————————————')
# 在需要比较字符串的程序中使用字符的多种表示会产生问题。
# 为了修正这个问题，可以使用unicodedata模块先将文本标准化
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))
# # normalize() 第一个参数指定字符串标准化的方式。
# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，而NFD表示字符应该分解为多个组合字符表示

print('————————————————————————————')
# Python同样支持扩展的标准化形式NFKC和NFKD，它们在处理某些字符的时候增加了额外的兼容特性
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

print('————————————————————————————')
print('清除掉一些文本上面的变音符')
t1 = unicodedata.normalize('NFD', s1)
a = ''.join(c for c in t1 if not unicodedata.combining(c))  # combining()测试一个字符是否为和音字符
print(a)