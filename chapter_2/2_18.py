# 字符串令牌解析

import re
from collections import namedtuple


text = 'foo = 23 + 42 * 10'

# 将字符串像下面这样转换为序列对
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# 利用命名捕获组的正则表达式来定义所有可能的令牌，包括空格
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'      # ?P<TOKENNAME> 用于给一个模式命名
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 令牌化，使用模式对象 scanner()
# scanner() 会创建一个 scanner 对象,在这个对象上不断的调用match()方法会一步步的扫描目标文本，每步一个匹配
scanner = master_pat.scanner('foo = 42')
print(scanner.match())
# print(_.lastgroup, _.group())       # '_'表示上一次执行的返回值,这里指scanner.match()
print(scanner.match().lastgroup, scanner.match().group())
print(scanner.match())
# print(scanner.match().lastgroup, scanner.match().group())
print(scanner.match())
# print(scanner.match().lastgroup, scanner.match().group())
print(scanner.match())
# print(scanner.match().lastgroup, scanner.match().group())
print(scanner.match())
# print(scanner.match().lastgroup, scanner.match().group())
print(scanner.match())


# 将上述令牌化代码打包到一个生成器中
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# 过滤令牌流，定义更多的生成器函数或者使用一个生成器表达式
print('——————————————————————————')
tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
for tok in tokens:
    print(tok)










