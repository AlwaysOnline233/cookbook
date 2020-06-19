# 只出现一次的数字
'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：算法应该具有线性时间复杂度。 可以不使用额外空间来实现吗？
示例:
输入: [2,2,1]        输出: 1
输入: [4,1,2,1,2]    输出: 4
来源：力扣（LeetCode）
'''

from collections import Counter


# Counter函数
class Solution:
    def singleNumber(self, nums):
        datas = Counter(nums)
        for each in datas:
            if datas[each] == 1:
                return each


# 位运算-异或(XOR)
class Solution2(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a


a = Solution()
print(a.singleNumber([2, 2, 1]))
print(a.singleNumber([4, 1, 2, 1, 2]))
b = Solution2()
print(b.singleNumber([2, 2, 1]))
print(b.singleNumber([4, 1, 2, 1, 2]))