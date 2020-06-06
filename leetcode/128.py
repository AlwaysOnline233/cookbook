#  最长连续序列
'''
给定一个未排序的整数数组，找出最长连续序列的长度。要求算法的时间复杂度为 O(n)
输入: [100, 4, 200, 1, 3, 2]        输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
来源：力扣（LeetCode）
'''

from typing import List


# 集合方式
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            # 判断是否是第一个数字
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)
        return res


# 字典方式
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                # 判断左右是否可以连起来
                left = lookup[num - 1] if num - 1 in lookup else 0
                right = lookup[num + 1] if num + 1 in lookup else 0
                # 记录长度
                lookup[num] = left + right + 1
                # 把头尾都设置为最长长度
                lookup[num - left] = left + right + 1
                lookup[num + right] = left + right + 1
                res = max(res, left + right + 1)
        return res


a = Solution()
print(a.longestConsecutive([100, 4, 200, 1, 3, 2]))
b = Solution2()
print(a.longestConsecutive([100, 4, 200, 1, 3, 2]))