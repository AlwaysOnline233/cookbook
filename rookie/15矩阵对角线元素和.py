# 矩阵对角线元素和


def f(lst):
    sum = 0
    for n in range(3):
        sum += lst[n][n]
    return sum


lst = [
    [3, 5, 6],
    [4, 7, 8],
    [2, 4, 9]
]
print(f(lst))
