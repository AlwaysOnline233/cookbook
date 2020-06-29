# 数组中的第K个最大元素
'''
在未排序的数组中找到第 k 个最大的元素。
注意，需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例：
输入: [3,2,1,5,6,4] 和 k = 2               输出: 5
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4         输出: 4
可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
来源：力扣（LeetCode）
'''


class Solution:
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


class Solution2:
    def findKthLargest(self, nums, k):
        """堆排序思想"""
        def heapify(a, start, end):
            """ 自上向下堆化
            Args:
                a (list): 输入数组
                start (int): 堆化目标在数组的位置
                end (int): 堆在数组的截止位置
            """
            while True:
                max_pos = start      # 初始化最大值所在位置为目标所在
                if start*2 + 1 <= end and a[start] < a[start*2+1]:
                    # 如果左叶子节点存在，且大于目标值，则将最大值所在位置指向该节点所在位置
                    max_pos = start*2 + 1
                if start*2 + 2 <= end and a[max_pos] < a[start*2+2]:
                    # 如果右叶子节点存在，且大于目标值，则将最大值所在位置指向该节点所在位置
                    max_pos = start*2 + 2
                if max_pos == start:
                    # 如果目标即为最大，完成该节点堆化，跳出循环
                    break
                # 交换位置，将最大值
                a[start], a[max_pos] = a[max_pos], a[start]
                start = max_pos

        # 建堆,只需要对前半节点堆化
        for i in range(len(nums)//2-1, -1, -1):
            heapify(nums, i, len(nums)-1)
        # 排序，只需要循环K次，排序TOP K个节点
        i = len(nums) - 1
        while i > len(nums) - 1 - k:
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            heapify(nums, 0, i)
        return nums[len(nums)-k]


b = Solution2()
print(b.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(b.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
