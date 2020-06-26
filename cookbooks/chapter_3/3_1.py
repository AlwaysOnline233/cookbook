# 数字的四舍五入

print('——————————————————————')
# 简单的舍入运算使用内置的 round(value, ndigits)
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361,3))

print('——————————————————————')
# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数
# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面
a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

print('——————————————————————')
# 不推荐             #  推荐 decimal 模块  （3_2.py）
a = 2.1
b = 4.2
c = a + b
print(c)            # 6.300000000000001
c = round(c, 2)
print(c)            # 6.3