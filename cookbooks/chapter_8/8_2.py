# 自定义字符串的格式化

from datetime import date

# 定义 __format__() 方法
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
    }


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2020, 6, 6)
print(format(d))
print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))


# datetime 模块
s = date(2020, 6, 6)
print(format(s))
print(format(s, '%A, %B %d, %Y'))
print('The end is {:%d %b %Y}. Goodbye'.format(s))
