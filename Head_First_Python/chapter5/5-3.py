# 函数串链
# 方法串链从左向右读，函数串链从右向左读

# 数据格式不统一
# python 对字符排序时，短横线优先点号优先冒号

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


with open('james.txt') as jaf:         # 打开文件
    data = jaf.readline()              # 读数据行
james = data.strip().split(',')        # 将数据转换为一个列表
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')  # data.strip().split(',') 方法串链  strip()去除字符串中空白符，split(',')创建一个列表
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

# sort()和 sorted() 默认升序排序，传入参数reverse=True降序排序

# 第31行代码至48行代码可以用列表推导代码替换
print('————————列表推导————————————')    # 5-4 列表推导
print(sorted([sanitize(t) for t in james]))    # 将列表转换为经过清理的有序版本
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))