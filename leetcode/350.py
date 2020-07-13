# 两个数组的交集 II
'''
给定两个数组，编写一个函数来计算它们的交集。
示例：
输入：nums1 = [1,2,2,1], nums2 = [2,2]       输出：[2,2]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
'''

# 方法一：哈希表
'''
由于同一个数字在两个数组中都可能出现多次，需要用哈希表存储每个数字出现的次数。对于一个数字，其在交集中出现的次数等于该数字在两个数组中出现次数的最小值。
首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，然后遍历第二个数组，
对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。
为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集
'''


'''
方法二：排序
如果两个数组是有序的，则可以便捷地计算两个数组的交集。
首先对两个数组进行排序，然后使用两个指针遍历两个数组。
初始时，两个指针分别指向两个数组的头部。每次比较两个指针指向的两个数组中的数字，如果两个数字不相等，则将指向较小数字的指针右移一位，
如果两个数字相等，将该数字添加到答案，并将两个指针都右移一位。当至少有一个指针超出数组范围时，遍历结束。
'''
class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1
        return intersection


a = Solution()
print(a.intersect([1, 2, 2, 1], [2, 2]))
print(a.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
