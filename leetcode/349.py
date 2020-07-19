# 两个数组的交集
'''
给定两个数组，编写一个函数来计算它们的交集
示例：   输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]   输出：[9,4]
说明：输出结果中的每个元素一定是唯一的。可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
'''


class Solution:
    # set 实现
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    # 内置函数
    def intersection2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)


a = Solution()
print(a.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(a.intersection2([1, 2, 2, 1], [2, 2]))
