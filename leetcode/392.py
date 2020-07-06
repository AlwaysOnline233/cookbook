#  判断子序列
'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
示例:
s = "abc", t = "ahbgdc"            返回 true
s = "axc", t = "ahbgdc"            返回 false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = q = 0
        cnt = 0
        while p < len(s) and q < len(t):
            if s[p] == t[q]:
                cnt += 1
                p += 1
            q += 1
        return cnt == len(s)

