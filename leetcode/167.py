# 两数之和 II - 输入有序数组
'''
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
输入: numbers = [2, 7, 11, 15], target = 9         输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
'''


class Solution:
    # 双指针
    def twoSum(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]

    # 二分查找
    def twoSum2(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1
        return [-1, -1]


a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))
print(a.twoSum2([2, 7, 11, 15], 22))
