# 外观数列

# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
# 注意：整数序列中的每一项将表示为一个字符串。
'''
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1                1 被读作  "one 1"  ("一个一") , 即 11
2.     11               11 被读作 "two 1s" ("两个一"）, 即 21
3.     21               21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211
4.     1211
5.     111221

示例
输入: 4       输出: "1211"
解释：当n=3时，序列是"21",其中有"2"和"1"两组，"2"读作"12",出现频次=1而值=2；类似"1"可以读作"11"。所以答案是"12"和"11"组合在一起，也就是"1211"。

来源：力扣（LeetCode）
'''

'''
思路：
先设置上一人为'1'
开始外循环
每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):                 # 每次外循环含义为给定上一个人报的数，求下一个人报的数
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):                # 每次内循环为遍历上一个人报的数
                if prev_person[j] == num:count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person


a = Solution()
print(a.countAndSay(4))
print(a.countAndSay(5))
print(a.countAndSay(10))
