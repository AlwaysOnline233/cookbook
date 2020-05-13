# 通过某个字段将记录分组  itertools.groupby()

from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))  # Sort by the desired field first
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

print('——————————————————————————————')
rows_by_date = defaultdict(list)        # 构建多值字典
for row in rows:
    rows_by_date[row['date']].append(row)
print('对指定日期访问对应的记录')
for r in rows_by_date['07/01/2012']:
    print(r)