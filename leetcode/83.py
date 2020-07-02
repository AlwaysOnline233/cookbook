# 删除排序链表中的重复元素
'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例 :
输入: 1->1->2           输出: 1->2
输入: 1->1->2->3->3     输出: 1->2->3
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        child = self.deleteDuplicates(head.next)
        if child and head.val == child.val:
            head.next = child.next
            child.next = None

        return head


