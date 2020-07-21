# 统计有序矩阵中的负数
'''
给一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
统计并返回 grid 中 负数 的数目。
示例：
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix
'''


class Solution:
    def countNegatives(self, grid):
        total = 0
        for item in grid:
            for num in item:
                if num < 0:
                    total += 1
        return total

    def countNegatives2(self, grid):
        total = 0
        i, j = 0, len(grid[0]) - 1

        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                total += len(grid) - i
                j -= 1
        # print(len(grid))
        return total


a = Solution()
print(a.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(a.countNegatives2([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
