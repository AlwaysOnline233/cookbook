# 最长连续递增序列
'''
给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。
示例: 输入: [1,3,5,4,7]      输出: 3       解释: 最长连续递增序列是 [1,3,5], 长度为3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
'''
'''
滑动窗口
每个（连续）增加的子序列是不相交的，并且每当 nums[i-1]>=nums[i] 时，每个此类子序列的边界都会出现。
当它这样做时，它标志着在 nums[i] 处开始一个新的递增子序列，我们将这样的 i 存储在变量 anchor 中。
'''


class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


a = Solution()
print(a.findLengthOfLCIS([1, 3, 5, 4, 7]))
print(a.findLengthOfLCIS([2, 2, 2, 2, 2]))