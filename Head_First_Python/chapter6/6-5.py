# 类     将代码及其数据打包在类中
# 类在所有对象实例间，方法共享，属性不共享
# 类中方法的第一个参数为self


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):        # 初始化
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def how_big(self):
        return (len(self.thing))


# a = Athlete() ,     python 处理代码时，Athlete().__init__(a)
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
print(type(sarah))
print(type(james))
print(sarah)             # sarah 与 james 内存地址不同
print(james)
print(sarah.name)
print(james.name)
print(sarah.dob)
print(james.dob)
print(sarah.times)
print(james.times)