class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


class Solution2:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x % 10 == 0 and x != 0:
            return False
        else:
            revert = 0
            while x > revert:
                revert = revert * 10 + x % 10
                x = x // 10              # x//10 表示x除以10 的商再取int()函数
            return x == revert or x == revert //10


a = Solution()
print(a.isPalindrome(121))
print(a.isPalindrome(-121))
b = Solution2()
print(b.isPalindrome(121))
print(b.isPalindrome(-121))