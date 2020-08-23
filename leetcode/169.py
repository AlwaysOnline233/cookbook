# 多数元素
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例: 输入: [3,2,3]    输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
'''
import collections
import random


class Solution:
    # 哈希表
    # 出现次数最多的元素大于 2/n 次，所以可以用哈希表来快速统计每个元素出现的次数
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 排序
    # 将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为 n/2 的元素（下标从 0 开始）一定是众数
    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    # 随机化
    # 因为超过 n/2 的数组下标被众数占据了，这样我们随机挑选一个下标对应的元素并验证，有很大的概率能找到众数
    def majorityElement3(self, nums):
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

    # 分治
    # 如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。
    '''
    使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
    如果回溯后某区间的长度大于 1，我们必须将左右子区间的值合并。如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
    否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数
    '''
    def majorityElement4(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right
        return majority_element_rec(0, len(nums) - 1)


a = Solution()
print(a.majorityElement([3, 2, 3]))
print(a.majorityElement2([3, 2, 3]))
print(a.majorityElement3([2, 2, 1, 1, 1, 2, 2]))
print(a.majorityElement4([2, 2, 1, 1, 1, 2, 2]))
