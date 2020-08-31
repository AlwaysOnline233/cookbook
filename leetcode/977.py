# 有序数组的平方
'''
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
'''


class Solution:
    # 排序
    def sortedSquares(self, A):
        result = sorted(x * x for x in A)
        return result

    # 双指针
    def sortedSquares2(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i] ** 2 < A[j] ** 2:
                ans.append(A[i] ** 2)
                i -= 1
            else:
                ans.append(A[j] ** 2)
                j += 1

        while i >= 0:
            ans.append(A[i] ** 2)
            i -= 1
        while j < N:
            ans.append(A[j] ** 2)
            j += 1
        return ans


a = Solution()
print(a.sortedSquares([-4, -1, 0, 3, 10]))
print(a.sortedSquares2([-7, -3, 2, 3, 11]))