#  罗马数字转整数
'''
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如，罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常，小的数字在大的数字的右边。但也存在特例，如4是IV。数字1在5的左边，所表示的数等于大数5减小数1得到的数值4。同样地，9表示IX。
这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

示例：
输入: "III"        输出: 3
输入: "MCMXCIV"    输出: 1994        解释: M = 1000, CM = 900, XC = 90, IV = 4.
来源：力扣（LeetCode）
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]]>=roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s)-1]
        num = num + roma_nums[last_num]
        return num


a = Solution()
print(a.romanToInt('III'))
print(a.romanToInt('IV'))
print(a.romanToInt('IX'))
print(a.romanToInt('LVIII'))
print(a.romanToInt('MCMXCIV'))