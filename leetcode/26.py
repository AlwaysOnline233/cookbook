# 删除排序数组中的重复项
'''
给定一个排序数组，需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
示例：
给定数组 nums = [1,1,2], 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
给定 nums = [0,0,1,1,1,2,2,3,3,4],返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

来源：力扣（LeetCode）
'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre, cur = 0, 1
        while cur < len(nums):
            if nums[pre] == nums[cur]:
                nums.pop(cur)
            else:
                pre = pre+1
                cur = cur+1
        # print(nums)
        return len(nums)


a = Solution()
print(a.removeDuplicates([1, 1, 2]))
print(a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
