# 在正则式中使用Unicode

import re

num = re.compile('\d+')      # \\d 匹配任意的unicode数字字符
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))


# 使用Unicode字符对应的转义序列(如 \uFFF 或者 \UFFFFFFF,包含指定的Unicode字符
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')


pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
a = pat.match(s)
print(a)
pat.match(s.upper())
print(s.upper())

# 当执行匹配和搜索操作的时候，最好是先标准化并且清理所有文本为标准化格式