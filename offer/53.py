# 0～n-1中缺失的数字
'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
示例:
输入: [0,1,2,3,4,5,6,7,9]       输出: 8
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
'''


class Solution:
    def missingNumber(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i


a = Solution()
print(a.missingNumber([0, 1, 3]))
print(a.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
