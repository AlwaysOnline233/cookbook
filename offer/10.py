# 斐波那契数列
'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
'''


# 递归
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return self.fib(n-1) + self.fib(n-2)
a = Solution()
print(a.fib(5))


# 动态规划
# 以斐波那契数列性质 f(n + 1) = f(n) + f(n - 1)f(n+1)=f(n)+f(n−1) 为转移方程
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007

print(fib2(5))