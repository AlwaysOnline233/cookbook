# 第三大的数
'''
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
示例: 输入: [3, 2, 1]    输出: 1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/third-maximum-number
'''


class Solution:
    def thirdMax(self, nums):
        first = second = third = float('-inf')
        for num in nums:
            if num > third:  # 通过第3关
                if num < second:
                    third = num
                elif num > second:  # 通过第2关
                    if num < first:
                        third = second
                        second = num
                    elif num > first:  # 通过第1关
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third

    def thirdMax2(self, nums):
        ans = sorted(list(set(nums)))
        return ans[-3] if len(ans) > 2 else ans[-1]


a = Solution()
print(a.thirdMax([3, 2, 1]))
print(a.thirdMax2([2, 2, 3, 1]))