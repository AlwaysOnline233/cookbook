# 比较三个数大小


# if和else实现
def f1(a, b, c):
    if a > b:
        if b > c:
            print(c, b, a)
        else:
            if a > c:
                print(b, c, a)
            else:
                print(b, a, c)
    elif a < b:
        if b < c:
            print(a, b, c)
        else:
            if c > a:
                print(a, c, b)
            else:
                print(c, a, b)

f1(1, 2, 3)
f1(2, 1, 2)


# 引入列表
def f2(nums):
    if nums[0] > nums[1]:
            if nums[0] > nums[2]:
                i3 = nums[0]
                if nums[1] > nums[2]:
                    i2 = nums[1]
                    i1 = nums[2]
                else:
                    i2 = nums[2]
                    i1 = nums[1]
            else:                 # 0<2  1<0
                    i3 = nums[2]
                    i2 = nums[0]
                    i1 = nums[1]
    else:                         # [0]<[1]
        if nums[0] < nums[2]:
            i1 = nums[0]
            if nums[1] < nums[2]:
                i2 = nums[1]
                i3 = nums[2]
            else:                 # [1]>[2]
                i2 = nums[2]
                i3 = nums[1]
        else:                     # [0]>[2]
            i1 = nums[2]
            i2 = nums[0]
            i3 = nums[1]
    print(i1, i2, i3)

f2([3, 1, 2])
f2([3, 2, 1])
f2([9, 5, 2])
f2([1, 3, 2])
f2([1, 3, 0])


# Max函数       (从大到小输出)
def f3(nums):
    while True:          # 此处不能使用for循环，不能一边迭代该列表，同时删除或者增加该列表
        x = max(nums)
        print(x)
        nums.remove(x)
        if len(nums) == 1:
            print(nums[0])
            break

f3([3, 2, 1])
f3([1, 2, 2])


# 用列表的sort()
nums = [10, 5, 5]
nums.sort()
print(nums)