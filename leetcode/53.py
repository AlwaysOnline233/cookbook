# 最大子序和
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''


class Solution:
    # 贪心
    # 若当前指针所指元素之前和小于0，则丢弃当前元素之前的数列
    def maxSubArray(self, nums):
        if not nums:return -2147483648       # 设置边界条件
        cur_sum = max_sum = nums[0]          # 初始值为列表第一个元素
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])  # 若当前指针所指元素之前和小于0，则丢弃当前元素之前的数列
            max_sum = max(cur_sum, max_sum)
        return max_sum

    # 动态规划
    # 若前一个元素大于0，则将其加到当前元素上
    def maxSubArray2(self, nums):
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i - 1]       # 若前一个元素大于0，则将其加到当前元素上
        return max(nums)               # 返回数组中的最大值


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(a.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

