# 字符串忽略大小写的搜索替换

import re

# 提供re.IGNORECASE 标志参数
text = 'UPPER PYTHON, lower python, Mixed Python'
a = re.findall('python', text, flags=re.IGNORECASE)
print(a)
b = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(b)     # 替换字符串并不会自动跟被匹配字符串的大小写保持一致


# 辅助函数保持大小写一致
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


c = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(c)
print("matchcase('snake')返回了一个回调函数(参数必须是match对象),sub()除接受替换字符串外，还能接受一个回调函数")