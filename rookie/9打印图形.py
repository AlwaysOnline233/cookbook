# 打印图形

rows = int(input('输入列数： '))
i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数

# 三角形
print("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" * ", end='')  # 注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print("\n")

print("等腰直角三角形2")
for i in range(1, rows + 1):
    print("*" * i, end='')
    print()

print("等边三角形1")
for i in range(1, rows + 1):  # 变量i控制行数
    for j in range(1, (rows + 1) - i):
        print(' ', end='')
    for k in range(1, 2 * i):
        print('*', end='')
    print()

print('等边三角形2')
for i in range(1, rows + 1):    # 控制三角形的高,也就是层数
    for j in range(2*(rows - i)):    # 控制每层第一个*的空格,从最后一层往上数分别是0, 2, 4, 6...,刚好是2n-2i
        print(" ", end="")
    for k in range(1, 2*i):     # 控制每层*的个数,由于是1,3,5,7,9...所以很快知道是2i-1
            print("*", end=' ')
    print()

print('空心等边三角形')
for i in range(1, rows + 1):       # 控制三角形的高,也就是层数
    for j in range(2*(rows-i)):    # 控制空格
        print(" ", end="")
    if 1 < i < rows:
        print("*", end="")
        for k in range(1, (2*(i-1)-1)*2 + 1 + 1):
                print(" ", end='')
        print("*", end="")
    else:
        for k in range(1, 2*i):    # 控制每层*的个数,由于是1,3,5,7,9...所以很快知道是2i-1
                print("*", end=' ')
    print()


# 打印菱形
print('菱形1')
b = rows
c = rows
for i in range(1, rows + 1):   # 先打印正三角，由空格和*根据规律组成
    print(" " * (b - 1), "*" * (2 * i - 1))
    b -= 1
    if i == rows:  # 临界点，当打印到此，开始打印倒三角
        for y in range(1, rows):
            print(" " * y, "*" * (2*c-3))
            c -= 1

print('菱形2')
list_a = [i for i in range(rows)]     # 生成前n行的行数列表，例如[0,1,2,3,4]
list_b = list_a[0:len(list_a) - 1:]   # 生成剩余行数列表并反转，例如[0,1,2,3]
list_c = list_b[::-1]                 # 对剩余行数列表并反转便于打印操作
list_d = list_a + list_c              # 将两个列表合并
# print(list_d)
b = [' ' * (rows - i) + '*' * (2 * i + 1) for i in list_d]   # 根据规律，打印空格" "和"*"
for line in b:
    print(line)

print('空心菱形')
b = rows
c = rows
print(" " * (rows - 1), "*")
for i in range(2, rows + 1):  # 先打印正三角，由空格和*根据规律组成
    print(" " * (b - 1) + "*" + " " * (2 * i - 3) + "*")
    b -= 1
    if i == rows:  # 临界点，当打印到此，开始打印倒三角
        for y in range(2, rows):
            print(" " * y+"*"+" "*(2*c-5)+ "*" )
            c -= 1
        print(" " * rows + "*")


# 正方形
print("实心正方形")
for i in range(0, rows):
    for j in range(0, rows):
        print(" * ", end='')     # 注意这里的","，一定不能省略，可以起到不换行的作用
        j += 1
    i += 1
    print()

print("空心正方形")
for i in range(0, rows):
    for j in range(0, rows):
        if i != 0 and i != rows - 1:
            if j == 0 or j == rows - 1:
                # 由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
                print(" * ", end='')     # 注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("   ", end='')      # 该处有三个空格
        else:
            print(" * ", end='')        # 这里*两侧加了空格
        j += 1
    i += 1
    print()
