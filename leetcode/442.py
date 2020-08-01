'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
不用到任何额外空间并在O(n)时间复杂度内解决这个问题
示例： 输入:[4,3,2,7,8,2,3,1]   输出:[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
'''


class Solution:
    # 通过索引号排序，比如数字4放到索引3的位置，最后找排序后数组，与索引号没有相差1便是重复元素
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                tmp = nums[i]
                # 注意要保持这个位置
                loc = nums[i] - 1
                nums[i] = nums[nums[i] - 1]
                nums[loc] = tmp
        for idx, val in enumerate(nums, 1):
            if val != idx:
                res.append(val)
        return res

    # 将元素转换成数组的索引并对应的将该处的元素乘以-1；
    # 若数组索引对应元素的位置本身就是负数，则表示已经对应过一次；在结果列表里增加该索引的正数就行；
    def findDuplicates2(self, nums):
        res = []
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                res.append(abs(n))
        return res


a = Solution()
print(a.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(a.findDuplicates2([4, 3, 2, 7, 8, 2, 3, 1]))