# 继承类


class NamedList(list):             # python内置list类
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johnny = NamedList('John Paul Jones')    # 创建一个新的对象实例
print(type(johnny))
print(dir(johnny))

# 使用list类提供的一些功能来补充johnny中存储的数据
johnny.append('Bass Player')
johnny.extend(['Composer', 'Arranger', 'Musician'])
print(johnny)
print(johnny.name)

# 由于　johnny是一个列表，所以可以对它做列表处理
for attr in johnny:
    print(johnny.name + 'is a ' + attr + '.')

