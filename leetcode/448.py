'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
不使用额外空间且时间复杂度为O(n)，可以假定返回的数组不算在额外空间内。
示例: 输入:[4,3,2,7,8,2,3,1]    输出:[5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
'''


class Solution(object):
    # 使用哈希表
    def findDisappearedNumbers(self, nums):
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not
        # really concerned with the frequency of numbers.
        hash_table = {}
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        # Response array that would contain the missing numbers
        result = []
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table.
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
        return result

    # 原地修改
    def findDisappearedNumbers2(self, nums):
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        # Response array that would contain the missing numbers
        result = []
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
        return result


a = Solution()
print(a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(a.findDisappearedNumbers2([4, 3, 2, 7, 8, 2, 3, 1]))
