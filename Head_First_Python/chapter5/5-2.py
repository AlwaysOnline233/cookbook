# 方法串链

# 依次打开4个数据文件，从文件读取数据行，由数据行创建一个列表
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

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))




