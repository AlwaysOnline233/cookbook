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


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')                       # 创建临时列表存放数据
        return (AthleteList(templ.pop(0), templ.pop(0), templ))     # 删除字典创建代码，替换对象创建代码
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "s fastest times are:" + str(james.top3()))
print(julie.name + "s fastest times are:" + str(julie.top3()))
print(mikey.name + "s fastest times are:" + str(mikey.top3()))
print(sarah.name + "s fastest times are:" + str(sarah.top3()))


