# 搜索插入位置
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
可以假设数组中无重复元素。
示例:
输入: [1,3,5,6], 5            输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
'''


class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l


a = Solution()
print(a.searchInsert([1, 3, 5, 6], 5))
print(a.searchInsert([1, 3, 5, 6], 2))
print(a.searchInsert([1, 3, 5, 6], 7))
print(a.searchInsert([1, 3, 5, 6], 0))
