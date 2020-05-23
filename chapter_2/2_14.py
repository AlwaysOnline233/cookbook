# 合并拼接字符串        join()

print('————————————————————————————')
print('用join()处理序列或者 iterable 中的合并的字符串')
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

print('————————————————————————————')
print('利用生成器表达式转换数据为字符串的同时合并字符串')
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print('————————————————————————————')
print('使用加号(+)处理合并少数的字符串')       # + 效率低
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a, b))

print('————————————————————————————')
print('将两个字面字符串合并起来，只需要简单的将它们放到一起')
a = 'Hello' 'World'
print(a)

print('————————————————————————————')
print('注意不必要的字符串连接操作')
print(a + ':' + b)        # Ugly
print(':'.join([a, b]))   # Still ugly
print(a, b, sep=':')      # Better

print('————————————————————————————')
print('使用生成器函数，利用yield语句产生输出片段')    # 编写构建大量小字符串的输出代码
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())        # 用 join() 将片段合并
print(text)

