# 顺时针打印矩阵
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
来源：力扣（LeetCode）
'''


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i])       # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])       # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i])   # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l])   # bottom to top
            l += 1
            if l > r: break
        return res


a = Solution()
print(a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(a.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))




