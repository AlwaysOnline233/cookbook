# 迭代删除重复项

'''
列表推导不能去除重复项，因为重复项的删除不是一个转换，算是一个过滤器。
重复项删除过滤器需要在列表创建过程中检查所创建的列表
'''


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')  # 方法串链  strip()去除字符串中空白符，split(',')创建一个列表
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(t) for t in james])   # 无序不一致的数据替换为经过清理的有序副本
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])

unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])

# 删除重复，得到最快的3次时间