# 给定一个头节点为 head 的单链表用于记录一系列核心肌群训练编号，请将该系列训练编号 倒序 记录于链表并返回。
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        res = dummy
        while head:
            tmp = ListNode()
            tmp.val = head.val
            tmp.next = None
            dummy.next = tmp
            dummy = dummy.next
            head = head.next
        return res.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

cls = Solution()
res = cls.trainningPlan(head)

# 遍历res
while res:
    print(res.val, end=' -> ')
    res = res.next
