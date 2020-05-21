# 推导列表
'''
1) 创建一个新列表来存放转换后的数据
2）迭代处理原列表中的各个数据项
3）每次迭代时完成转换
4）将转换后的数据追加到新列表
clean_mikey = [sanitize(each_t) for each_t in mikey]
'''

print('—————分钟列表转换为秒列表————————')
mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print(secs)

print('—————米转换为英尺————————')
meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)

print('—————混合大小写和小写转换为全大写字符串————————')
lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


print('—————使用sanitize()将列表数据转换为格式正确的时间————————')
dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

print('—————列表转换的结果赋回原来的目标标识符————————')
clean = [float(s) for s in clean]        # 字符串列表转换为浮点数列表
print(clean)

print('—————函数链转换————————')
clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)