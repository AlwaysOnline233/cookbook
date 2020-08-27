# 最接近的三数之和
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        # nums = dict(enumerate(nums))
        length = len(nums)
        # 初始为无穷大
        res = float('inf')
        for begin in range(length):
            start = begin + 1
            stop = length - 1
            while start < stop:
                add_value = nums[begin] + nums[start] + nums[stop]
                if add_value < target:
                    start += 1
                elif add_value > target:
                    stop -= 1
                else:
                    return add_value

                if abs(res - target) > abs(add_value - target):
                    res = add_value
        return res


a = Solution()
print(a.threeSumClosest([-1, 2, 1, -4], 1))
