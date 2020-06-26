# 解压可迭代对象赋值给多个变量    * 解压不确定个数

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record  # 解压出的phone_numbers是列表类型
print(name)
print(email)
print(phone_numbers)

print('————————————————————————————')
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]  # 前7个与最后1个对比
print(trailing)
print(current)


# *在迭代元素为可变长元组的序列很有用
print('————————————————————————————')
reconds = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in reconds:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# *解压语法在字符串操作很有用，比如字符串分割
print('————————————————————————————')
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)


# 丢弃一些元素
print('————————————————————————————')
note = ('ACME', 50, 123.45, (12, 18,  2012))
na, *_, (*_, year) = note
print(na)
print(year)


# 分割法实现递归
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


items = [1, 10, 7, 4, 5, 9]
x = sum(items)
print(x)
