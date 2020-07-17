# 大小为 K 且平均值大于等于阈值的子数组数目
'''
给一个整数数组arr和两个整数k和threshold。返回长度为k且平均值大于等于threshold的子数组数目。
示例：
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组[2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。

来源：力扣（LeetCode）
'''


# 每次以k个数为一个窗口进行滑动，addRes用来保存连续k个数的和，滑动一次，加上新的数减去左侧丢掉的数，重新判断
class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        if len(arr) < k:
            return 0
        addRes = sum(arr[:k])
        res = 0
        target = k*threshold
        if addRes >= target:
            res += 1
        for i in range(k, len(arr)):
            addRes = addRes + arr[i] - arr[i-k]
            if addRes >= target:
                res += 1
        return res


a = Solution()
print(a.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
print(a.numOfSubarrays([1, 1, 1, 1, 1], 1, 0))
print(a.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
