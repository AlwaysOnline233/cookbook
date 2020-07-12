# 二分查找
'''
给定一个n个元素有序的（升序）整型数组 nums 和一个目标值 target ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例：
输入: nums = [-1,0,3,5,9,12], target = 9           输出: 4
解释: 9 出现在 nums 中并且下标为 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
'''


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


a = Solution()
print(a.search([-1, 0, 3, 5, 9, 12], 9))
print(a.search([-1, 0, 3, 5, 9, 12], 2))