# 用Shell通配符匹配字符串      fnmatch()  fnmatchcase()

from fnmatch import fnmatch, fnmatchcase

a = fnmatch('foo.txt', '*.txt')     # fnmatch()函数使用底层操作系统的大小写敏感规则(不同系统是不一样)匹配模式
print(a)
a1 = fnmatch('foo.txt', '*.Txt')    # Mac区分大小写   Windows不区分
print(a1)
b = fnmatch('foo.txt', '?oo.txt')
print(b)
c = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(c)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
d = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(d)

print('————————————————————————————')    # fnmatchcase()完全区分大小写
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
x = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(x)
y = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(y)


