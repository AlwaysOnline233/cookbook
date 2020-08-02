'''
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例:  输入: [1,2,0]    输出: 3
提示：算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
'''


class Solution:
    # 将数组视为哈希表
    # 对于一个长度为N的数组，其中没有出现的最小正整数只能在[1, N+1]中。
    # 这是因为如果[1,N]都出现了，那么答案是N+1，否则答案是[1,N]中没有出现的最小正整数
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


a = Solution()
print(a.firstMissingPositive([1, 2, 0]))
print(a.firstMissingPositive([3, 4, -1, 1]))
print(a.firstMissingPositive([7, 8, 9, 11, 12]))
