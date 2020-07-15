# 寻找比目标字母大的最小字母
'''
给一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
示例：
输入: letters = ["c", "f", "j"]       target = "a"        输出: "c"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target
'''
import bisect


class Solution(object):
    '''
    线性扫描
    由于 letters 已经有序，当我们从左往右扫描找到比目标字母大字母则该字母就是答案。否则(letters 不为空)答案将是 letters[0]
    '''
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]

    # 二分查找
    def nextGreatestLetter2(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


a = Solution()
print(a.nextGreatestLetter(["c", "f", "j"], 'a'))
print(a.nextGreatestLetter(["c", "f", "j"], 'c'))
print(a.nextGreatestLetter(["c", "f", "j"], 'd'))
print(a.nextGreatestLetter2(["c", "f", "j"], 'g'))
print(a.nextGreatestLetter2(["c", "f", "j"], 'j'))
print(a.nextGreatestLetter2(["c", "f", "j"], 'k'))


# bisect是python内置模块，用于有序序列的插入和查找
a = [1, 4, 6, 8, 12, 15, 20]
position = bisect.bisect(a, 13)
print(position)      # 5

# 用可变序列内置的insert方法插入
a.insert(position, 13)
print(a)         # [1, 4, 6, 8, 12, 13, 15, 20]
