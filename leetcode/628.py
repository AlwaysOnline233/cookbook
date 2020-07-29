# 三个数的最大乘积
'''
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
示例： 输入: [1,2,3,4]     输出: 24
'''


class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])

    def maximumProduct2(self, nums):
        max1 = -float('inf')
        max2 = -float('inf')
        max3 = -float('inf')
        min1 = float('inf')
        min2 = float('inf')

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)


a = Solution()
print(a.maximumProduct([1, 2, 3]))
print(a.maximumProduct([1, 2, 3, 4]))
