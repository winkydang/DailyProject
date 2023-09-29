# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        return self.BFS(tree)

    def BFS(self, tree):
        que = collections.deque([tree])
        res = []
        while que:
            sz = len(que)
            t = ListNode(-1)
            p = t
            for i in range(sz):
                node = que.popleft()
                q = ListNode(node.val)
                p.next = q
                p = p.next

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(t.next)
        return res

# [1,2,3,4,5,null,7,8]
sol = Solution()
# tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), None), TreeNode(5))), TreeNode(3,None, TreeNode(7))
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t4.left = t8
t3.right = t7
t2.left = t4
t2.right = t5
t1.left = t2
t2.right = t3
res = sol.listOfDepth(t1)
print(res)
