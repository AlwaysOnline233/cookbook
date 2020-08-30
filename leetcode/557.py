# 反转字符串中的单词 III
'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
'''


class Solution:
    def reverseWords(self, s):
        return ' '.join(item[::-1] for item in s.split(' '))

    # 双指针
    def reverseWords2(self, s):
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s = s[:j] + s[j:i][::-1] + s[i:]
                j = i + 1
            elif i == len(s) - 1:
                s = s[:j] + s[j:][::-1]
        return s


a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))
print(a.reverseWords2("Let's take LeetCode contest"))