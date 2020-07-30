# 错误的集合
'''
集合S包含从1到n的整数。因为数据错误，导致集合里面某一个元素复制成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
给定一个数组 nums 代表了集合 S 发生错误后的结果。首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
示例: 输入: nums = [1,2,2,4]     输出: [2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
'''


class Solution:
    # 将nums的所有索引提取出一个数组idx，那么由idx和nums组成的数组构成singleNumbers的输入，其输出是唯二不同的两个数。
    # 但是不知道哪个是缺失的，哪个是重复的，因此需要重新进行一次遍历，判断出哪个是缺失的，哪个是重复的
    def singleNumbers(self, nums):
        ret = 0     # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while(ret & h == 0):
            h <<= 1
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
            else:
                b ^= n
        return [a, b]
    def findErrorNums(self, nums):
        nums = [0] + nums
        idx = []
        for i in range(len(nums)):
            idx.append(i)
        a, b = self.singleNumbers(nums + idx)
        for num in nums:
            if a == num:
                return [a, b]
        return [b, a]

    # 法2
    def findErrorNums2(self, nums):
        nums.sort()
        res = [0] * 2
        tmp = set(range(1, len(nums) + 1))
        for i in range(len(nums)):
            if nums[i] in tmp:
                tmp.remove(nums[i])
            else:
                res[0] = nums[i]
        res[1] = tmp.pop()
        return res


a = Solution()
print(a.findErrorNums([1, 2, 2, 4]))
print(a.findErrorNums2([1, 2, 2, 4]))
