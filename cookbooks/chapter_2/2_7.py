# 最短匹配模式

import re

str_pat1 = re.compile(r'"(.*)"')    # 贪婪模式 查找最长可能匹配
text1 = 'Computer says "no."'
a = str_pat1.findall(text1)
print(a)

str_pat2 = re.compile(r'"(.*?)"')   # 非贪婪模式 最短匹配
text2 = 'Computer says "no." Phone says "yes."'
b = str_pat2.findall(text2)
print(b)

# 点(.)匹配除了换行外的任何字符
# 在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配


