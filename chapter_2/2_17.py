# 在字符串中处理html和xml

import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

# html.escape() 替换文本字符串中的 ‘<’ 或者 ‘>’
s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))         # Disable escaping of quotes

print('——————————————————————————————')
# 处理ASCII文本,并且想将非ASCII文本对应的编码实体嵌入进去,可以给某些I/O函数传递参数 errors='xmlcharrefreplace'
s = 'Spicy Jalapeño'
ss = s.encode('ascii', errors='xmlcharrefreplace')
print(ss)

print('——————————————————————————————')
'''
替换文本中的编码实体，需要使用另外一种方法。如果正在处理HTML或者XML文本，先使用一个合适的HTML或者XML解析器。 
通常情况下，这些工具会自动替换这些编码值。
接收到一些含有编码值的原始文本，需要手动去做替换，通常只需要使用HTML或者XML解析器的一些相关工具函数/方法即可。
'''
s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
print(p.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))