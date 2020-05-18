# 列表

cast = ['Cleese', 'Palin', 'Jones', 'Idle']
print(cast)
print(len(cast))
print(cast[1])

cast.append('Gilliam')        # 列表末尾增加数据线append()
print(cast)
cast.pop()                    # 列表末尾删除数据pop()
print(cast)
cast.extend(['Gilliam', 'Chapman'])    # 列表末尾增加一个数据项集合extend()
print(cast)
cast.remove('Gilliam')        # 删除一个特定的数据项remove()
print(cast)
cast.insert(0, 'Gilliam')     # 在特定位置前增加一个数据项insert()
print(cast)


# 向列表增加更多数据
movies = ['The Holy Grail', 'The Life of Brain', 'The Meaning of Life']
# 法1）将年份插入列表
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)
# 法2）重新创建列表
movies = ['The Holy Grail', 1975,
          'The Life of Brain', 1979,
          'The Meaning of Life', 1983]
print(movies)
print('对于这样一个小列表来说，第2种方法更可取')


# 处理列表数据
# for迭代处理列表
fav_movies = ['The Holy Grail', 'The Life of Brain']
for each_flick in fav_movies:
    print(each_flick)

# while循环迭代
count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1


