# 整数反转
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例：
输入: 123        输出: 321
输入: -123       输出: -321
输入: 120        输出: 21
假设环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
如果反转后整数溢出那么就返回 0。
'''


class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >= 0 else -1    # x>=0,flag=1;反之flag=-1
        abs_x = abs(x)
        x_str = str(abs_x)
        reverse_x_str = x_str[::-1]
        reverse_x_int = int(reverse_x_str)*flag
        if -2**31 <= reverse_x_int <= 2**31 -1:
            return reverse_x_int
        else:
            return 0


a = Solution()
print(a.reverse(123))
print(a.reverse(-123))
print(a.reverse(120))