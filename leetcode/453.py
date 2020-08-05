'''
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n-1 个元素增加1。
示例:
 输入:[1,2,3]    输出:3    解释:需要3次移动：[1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements
'''


class Solution:
    # n-1个值加1等于1个值减1
    # 每次让一个值减去1，使得所有的值相等，理想情况是每个值最终等于最小值。题目转换为所有值减去最小值的和
    def minMoves(self, nums):
        minvalue = min(nums)
        count = 0
        for i in nums:
            count += i - minvalue
        return count


a = Solution()
print(a.minMoves([1, 2, 3]))
