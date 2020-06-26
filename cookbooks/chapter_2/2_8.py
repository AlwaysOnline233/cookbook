# 多行匹配模式

import re

comment = re.compile(r'/\*(.*?)\*/')    # 点(.)不能匹配换行符
text1 = '/* this is a comment */'
text2 = '''/* this is a 
 multiline comment */
        '''
a = comment.findall(text1)
b = comment.findall(text2)
print(a)
print(b)

# 修改模式字符串，增加对换行的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')  # (?:.|\n)指定了一个非捕获组(一个仅用来做匹配，而不能通过单独捕获或者编号的组)
c = comment.findall(text2)
print(c)

# re.compile() 函数接受一个标志参数 re.DOTALL,它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
d = comment.findall(text2)
print(d)


