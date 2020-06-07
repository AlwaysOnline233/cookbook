#  单词接龙

'''
给定两个单词（beginWord和endWord）和一个字典wordList,找出所有从 beginWord 到 endWord 的最短转换序列。
转换需遵循如下规则：
每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。
说明:
如果不存在这样的转换序列,返回一个空列表。所有单词具有相同的长度。所有单词只由小写字母组成。字典中不存在重复的单词。
可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

来源：力扣（LeetCode）
'''

from typing import List
import collections


# 广度搜索
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        dic = collections.defaultdict(list)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                dic[w[:i] + '*' + w[i+1:]].append(w)
        q, s = collections.deque([(beginWord, [beginWord])]), collections.deque()
        seen = set()
        res = []
        while q:
            while q:
                w, path = q.popleft()
                if w == endWord: res.append(path)
                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i+1:]]:
                        if v not in seen:
                            s.append((v, path + [v]))
            if res: return res
            q, s = s, q
        return []


a = Solution()
print(a.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]
))





