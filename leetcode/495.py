# 提莫攻击
'''
在《英雄联盟》中，有一个叫“提莫”的英雄，他的攻击可以让敌方英雄艾希进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，输出艾希的中毒状态总时长。
可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。
示例:  输入: [1,4], 2        输出: 4
原因: 第1秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持2秒钟，直到第2秒末结束。第4秒初，提莫再次攻击艾希，使得艾希获得另外2秒中毒时间。所以最终输出4秒。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/teemo-attacking
'''


class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration


a = Solution()
print(a.findPoisonedDuration([1, 4], 2))
print(a.findPoisonedDuration([1, 2], 2))
