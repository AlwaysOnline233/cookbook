# 数组的相对排序
'''
给两个数组，arr1 和 arr2，arr2 中的元素各不相同，arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
'''


class Solution:
    def relativeSortArray(self, arr1, arr2):
        my_arr = [0] * 1001      # 创建长度为1001，初值均为0的数组用于记录0-1000在arr1中出现的次数my_arr
        res = []
        for num in arr1:
            my_arr[num] += 1     # 遍历arr1并更新my_arr以记录各数字出现的次数

        for num in arr2:
            res += [num] * my_arr[num]   # 遍历arr2中各元素并根据其在arr1中出现的次数，将其添加到结果数组res,
            my_arr[num] = 0              # 并将其在my_arr中的值清零
        for i, num in enumerate(my_arr):
            if num != 0:
                res += [i] * num         # 遍历my_arr,对于其中非0元素num，将其下标重复num次添加到结果数组
        return res


a = Solution()
print(a.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))