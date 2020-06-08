# 最长公共子序列
'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
来源：力扣（LeetCode）
'''

class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        m, n = len(str1), len(str2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


a = Solution()
print(a.longestCommonSubsequence('abcde', 'ace'))