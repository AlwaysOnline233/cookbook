# 字节字符串上的字符串操作

import re

# 字节字符串同样也支持大部分和文本字符串一样的内置操作
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

print('——————————————————————————————')
# 这些操作同样也适用于字节数组
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

print('——————————————————————————————')
# 可以使用正则表达式匹配字节字符串，但是正则表达式本身必须也是字节串
data = b'FOO:BAR,SPAM'
# re.split('[:,]',data)   # TypeError: cannot use a string pattern on a bytes-like object
s = re.split(b'[:,]', data)    # Notice: pattern as bytes
print(s)

print('——————————————————————————————')
# 大多数情况下，在文本字符串上的操作均可用于字节字符串。然而，这里也有一些需要注意的不同点。
# 首先，字节字符串的索引操作返回整数而不是单独字符
a = 'Hello World'   # Text string
print(a[0])                # H
print(a[1])                # e
b = b'Hello World'  # Byte string
print(b[0])                # 72
print(b[1])                # 101

# 第二点,字节字符串不会提供一个美观的字符串表示，也不能很好的打印出来，除非先被解码为一个文本字符串
s = b'Hello World'
print(s)
print(s.decode('ascii'))

# 不存在任何适用于字节字符串的格式化操作
# 如果想格式化字节字符串，得先使用标准的文本字符串，然后将其编码为字节字符串
a = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(a)