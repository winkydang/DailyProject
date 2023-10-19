# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
# 返回删除后的链表的头节点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         if not head:
#             return None
#         if head.val == val and not head.next:
#             return None
#         dummy = ListNode(-1)
#         dummy = head
#         # 链表的遍历
#         while head and head.next:
#             if head.val == val:
#                 head = head.next
#             elif head.next.val == val:
#                 head.next = head.next.next
#                 return dummy
#             else:
#                 head = head.next
#         return dummy

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
            # 处理特殊情况，如果链表的第一个节点是待删除值
        if head.val == val:
            return head.next

        dummy = ListNode(-1)
        dummy = head  # 接下来head的值变动时，dummy的值不会跟着变；但是dummy的值变动时，head的值会跟着变动

        # 链表的遍历
        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
                return head
            dummy = dummy.next
        return head


# h = ListNode(-3, ListNode(5, ListNode(-99)))  -- 错误的初始化
# 创建链表: -3  ->  5  ->  -99
head = ListNode(-3)
head.next = ListNode(5)
head.next.next = ListNode(-99)
# val = -3
val = 5
cls = Solution()
res = cls.deleteNode(head, val)
# 打印结果链表
while res:
    print(res.val, end=' -> ')
    res = res.next
