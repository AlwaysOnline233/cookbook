'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
示例:   输入: [3,0,1]       输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
'''


class Solution:
    # 排序
    def missingNumber(self, nums):
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)            # Ensure that n is at the last index
        elif nums[0] != 0:
            return 0                    # Ensure that 0 is at the first index
        for i in range(1, len(nums)):   # the missing number is on the range (0, n)
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

    # 哈希表
    def missingNumber2(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    # 位运算
    def missingNumber3(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # 数学法  用高斯求和公式求出[0..n]的和，减去数组中所有数的和，就得到了缺失的数字  n*(n+1)/2
    def missingNumber4(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


a = Solution()
print(a.missingNumber([3, 0, 1]))
print(a.missingNumber2([3, 0, 1]))
print(a.missingNumber3([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(a.missingNumber4([9, 6, 4, 2, 3, 5, 7, 0, 1]))
