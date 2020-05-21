# 将6-1.py中代码用字典替换


from chapter6.sanitize_fun import sanitize


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()               # 读入数据，在30行代码处创建字典。为什么不一次完成字典创建？（见6-4.py）
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)


sarah = get_coach_data('sarah2.txt')
# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)  # pop()从列表指定位置删除并发返回一个数据项
# print(sarah_name + "s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

# 删除上面两行代码，用字典来保存处理数据
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name'] + "s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))



