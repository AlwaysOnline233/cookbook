# 复写零
'''
给一个长度固定的整数数组 arr，将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
注意：不要在超过该数组长度的位置写入元素。
要求：对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
示例：
输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/duplicate-zeros
'''


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        length_ = len(arr) - 1
        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):
            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break
            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1
        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups
        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


arr = [1, 0, 2, 3, 0, 4, 5, 0]
a = Solution()
print(a.duplicateZeros(arr))
print(arr)
