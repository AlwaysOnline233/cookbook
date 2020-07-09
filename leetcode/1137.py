# 第 N 个泰波那契数
'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给整数 n，请返回第 n 个泰波那契数 Tn 的值。
示例：
输入：n = 4              输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
输入：n = 25            输出：1389537

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
'''


# 递归
class Solution:
    def tribonacci(self,n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n >= 3:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n-3)


a = Solution()
print(a.tribonacci(25))


# 迭代
def tribonacci2(n):
    if n == 0:return 0
    if n == 1:return 1
    if n == 2:return 1
    a, b, c = 0, 1, 1
    while n > 2:
        res = a+b+c
        a, b, c = b, c, res
        n -= 1
    return res


print(tribonacci2(4))