#  两数之和
'''
给定一个整数数组 nums 和一个目标值 target
在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
来源：力扣（LeetCode）
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))
print(a.twoSum([2, 11, 7, 15], 9))

b = Solution2()
print(b.twoSum([2, 7, 11, 15], 9))
print(b.twoSum([2, 11, 7, 15], 9))