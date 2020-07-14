# 寻找重复数
'''
给定一个包含n+1个整数的数组nums，其数字都在1到n之间，可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
示例：
输入: [1,3,4,2,2]       输出: 2
说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
'''


class Solution:
    def findDuplicate(self, nums):
        size = len(nums)
        left = 1
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里
            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left


a = Solution()
print(a.findDuplicate([1, 3, 4, 2, 2]))
print(a.findDuplicate([3, 1, 3, 4, 2]))