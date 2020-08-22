# 子数组最大平均数 I
'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
示例1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-i
'''


# 滑动窗口
class Solution:
    def findMaxAverage(self, nums, k):
        big = he = sum(nums[:k])
        size = len(nums)
        for j in range(k, size):
            he += nums[j] - nums[j - k]
            if he > big:
                big = he
        return big / k