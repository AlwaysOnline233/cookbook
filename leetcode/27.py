# 移除元素
'''
给一个数组 nums 和一个值 val，需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例:
给定 nums = [3,2,2,3], val = 3,函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
给定 nums = [0,1,2,2,3,0,4,2], val = 2,函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

来源：力扣（LeetCode）
'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


a = Solution()
print(a.removeElement([3, 2, 2, 3], 3))
print(a.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
