# 数组中的第K个最大元素
'''
在未排序的数组中找到第 k 个最大的元素。
注意，需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例：
输入: [3,2,1,5,6,4] 和 k = 2               输出: 5
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4         输出: 4
可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]


a = Solution()
print(a.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(a.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
