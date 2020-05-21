
from chapter6.sanitize_fun import sanitize


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')    # 创建临时列表存放数据
        return ({
            'Name': templ.pop(0),
            'DOB': templ.pop(0),
            'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])
        })
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james['Name'] + "s fastest times are:" + james['Times'])
print(julie['Name'] + "s fastest times are:" + julie['Times'])
print(mikey['Name'] + "s fastest times are:" + mikey['Times'])
print(sarah['Name'] + "s fastest times are:" + sarah['Times'])
