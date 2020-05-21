from chapter6.sanitize_fun import sanitize


# 类的方式实现前面得到3次最短时间的功能   在类中增加新功能

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')                       # 创建临时列表存放数据
        return (Athlete(templ.pop(0), templ.pop(0), templ))     # 删除字典创建代码，替换Athlete对象创建代码
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


vera = Athlete('Vera Vi')       # 创建一个新的对象实例
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top3())