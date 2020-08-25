# 统计好三元组
'''
给你一个整数数组 arr ，以及 a、b 、c 三个整数，统计其中好三元组的数量。
如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。
0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。
返回 好三元组的数量 。

示例 1：
输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-good-triplets
'''


class Solution:
    # 枚举
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1
        return cnt


a = Solution()
print(a.countGoodTriplets([3, 0, 1, 1, 9, 7], a=7, b=2, c=3))