# 最大连续1的个数
'''
给定一个二进制数组， 计算其中最大连续1的个数。
示例: 输入: [1,1,0,1,1,1]   输出: 3
注意：
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones
'''


class Solution:
    '''
    一次遍历
    用一个计数器 count 记录 1 的数量，另一个计数器 maxCount 记录当前最大的 1 的数量。
    当遇到 1 时，count 加一。
    当遇到 0 时：将 count 与 maxCount 比较，maxCoiunt 记录较大值。将 count 设为 0。
    返回 maxCount
    '''
    def findMaxConsecutiveOnes(self, nums):
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)

    '''
    使用 map 和 join 来解决此问题。
    使用 splits 函数在 0 处分割将数组转换成字符串。在获取子串的最大长度就是最大连续 1 的长度
    '''
    def findMaxConsecutiveOnes2(self, nums):
        return max(map(len, ''.join(map(str, nums)).split('0')))
