# 使用字典关联数据    字典：内置的数据结构，允许将数据与键而不是数字关联

cleese = {}         # 大括号创建空字典
palin = dict()      # 工厂函数dict()创建空字典
print(type(cleese))
print(type(palin))

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}
print(palin['Name'])    # 使用中括号指定字典中的索引来访问数据项  键作为索引
print(cleese['Occupations'][-1])    # 使用数字来访问存储在特定字典键位置上的列表项

print('增加出生地数据')
palin['Birthplace'] = 'Broomhill, Sheffield, England'   # 字典不会维护插入顺序
cleese['Birthplace'] = 'Weston-super-Mare, North Somerset, England'
print(palin)
print(cleese)


