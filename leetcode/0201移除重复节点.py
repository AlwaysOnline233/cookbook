# 移除重复节点
'''
移除未排序链表中的重复节点。保留最开始出现的节点
示例:
输入：[1, 2, 3, 3, 2, 1]      输出：[1, 2, 3]
'''

'''
解题思路：
用set做临时缓冲区
循环链表，判断当前节点的值是否存在set中
未在set中的值放在set中，如在set中则重连链表
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head


