# 跳水板
'''
正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
返回的长度需要从小到大排列。
示例：
输入：shorter = 1        longer = 2         k = 3
输出： {3,4,5,6}
解释：3 = 1 + 1 + 1
     4 = 1 + 1 + 2
     5 = 1 + 2 + 2
     6 = 2 + 2 + 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diving-board-lcci
'''


# 等差数列
class Solution:
    def divingBoard(self, shorter, longer, k):
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        delta = longer - shorter
        return [k * shorter + delta * i for i in range(k + 1)]


a = Solution()
print(a.divingBoard(1, 2, 3))

