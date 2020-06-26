# 清理审查文本字符串

'''
str.upper() 和 str.lower()将文本转为标准格式。
str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定的字符序列
unicodedata.normalize() 函数将unicode文本标准化
'''

import unicodedata
import sys

print('消除整个区间上的字符或者去除变音符：')
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

print('1.清理空白字符：')
remap = {                             # 创建一个小的转换表格
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)

print('2.删除所有的和音符')
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b.translate(cmb_chrs))
