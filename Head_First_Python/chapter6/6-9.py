from chapter6.sanitize_fun import sanitize


# 继承内置list类
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):                                              # self.times  cf  self
        return (sorted(set([sanitize(t) for t in self]))[0:3])   # 数据本身是计时数据，这里不再需要times


vera = AthleteList('Vera Vi')       # 创建一个新的对象实例
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())