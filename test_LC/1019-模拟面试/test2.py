# LC24: 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        # dummy = ListNode(-1, head)

        pre = dummy

        p = dummy.next

        while p and p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = p
            pre.next = tmp

            pre = p
            p = p.next
        return dummy.next