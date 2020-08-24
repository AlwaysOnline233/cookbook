# 重复的子字符串
'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例1:    输入: "abab"      输出: True       解释: 可由子字符串 "ab" 重复两次构成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-substring-pattern
'''


class Solution:
    # 枚举
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False

    # 字符串匹配
    def repeatedSubstringPattern2(self, s):
        return (s + s).find(s, 1) != len(s)

    # KMP 算法
    def repeatedSubstringPattern3(self, s: str) -> bool:
        def kmp(query: str, pattern: str) -> bool:
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            match = -1
            for i in range(1, n - 1):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return True
            return False
        return kmp(s + s, s)


a = Solution()
print(a.repeatedSubstringPattern('abab'))
print(a.repeatedSubstringPattern('aba'))
print(a.repeatedSubstringPattern('abcabcabcabc'))
