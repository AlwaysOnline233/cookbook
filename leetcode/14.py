# 最长公共前缀
'''
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
说明:所有输入只包含小写字母 a-z
示例
输入: ["flower","flow","flight"]        输出: "fl"
输入: ["dog","racecar","car"]           输出: ""          解释: 输入不存在公共前缀。
来源：力扣（LeetCode）
'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                res = res + i[0]
            else:
                break
        return res


a = Solution()
print(a.longestCommonPrefix(["flower", "flow", "flight"]))
print(a.longestCommonPrefix(["dog", "racecar", "car"]))





