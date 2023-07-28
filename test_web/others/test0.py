import os
from collections import Counter
from typing import List, Optional


# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
#
# titles = ["title1", "title2", "title3", "tilte4", "title5", "title6", "aaa"]
# unique_titles = []
#
# for title in titles:
#     if title not in unique_titles:
#         for unique_title in unique_titles:
#             similarity = fuzz.token_set_ratio(title, unique_title)
#             if similarity > 80:  # 设置相似度阈值
#                 break
#         else:
#             unique_titles.append(title)
#
# print(unique_titles)
# from typing import List
#
# def getFolderNames(names: List[str]) -> List[str]:
#     dic = {}
#     for name in names:
#         if name not in dic:
#             dic[name] = 1
#         else:
#             flag = dic[name]
#             while name + f'({flag})' in dic:
#                 flag += 1
#             dic[name] = flag
#             dic[name + f'({flag})'] = 1
#     return list(dic.keys())
#
# # names = ["kaido","kaido(1)","kaido","kaido(1)"]
# # names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
# # names = ["wano","wano","wano","wano"]
# names = ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
# print(getFolderNames(names))

# def countEven(num: int) -> int:
#     ans = 0
#     for i in range(1,num+1):
#         if sum(int(i) for i in str(i)) % 2 == 0:
#             ans += 1
#     return ans
# num = 4
# print(countEven(4))

# def isPalindrome(x: int) -> bool:
#     s = str(x)
#     s1 = ''
#     for i in s:
#         s1 = i + s1
#     if s == s1:
#         return True
#     else:
#         return False
# x = 121
# print(isPalindrome(x))

# def isPalindrome(x: int) -> bool:
#     if x < 0:
#         return False
#     num = x
#     cur = 0
#     while num > 0:
#         cur = cur * 10 + num % 10
#         num //= 10
#     if cur == x:
#         return True
#     else:
#         return False
# print(isPalindrome(121))
# def romanToInt(s: str) -> int:
#     dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     ans = 0
#     for i in range(len(s) - 1):
#         if dic[s[i]] >= dic[s[i+1]]:
#             ans += dic[s[i]]
#         else:
#             ans -= dic[s[i]]
#     ans += dic[s[-1]]
#     return ans
# print(romanToInt("LVIII"))

# str = 'abcdeffedcba*'
# for item in reversed(str):
#     print(item, end='')
# print()

# def isPalindrome(x: int) -> bool:
#     x = str(x)
#     s = ''
#     for item in reversed(x):
#         s = s + item
#     return x == s
# print(isPalindrome(121))

# def longestCommonPrefix(strs: List[str]) -> str:
#     ans = 0
#     m = len(strs)
#     n = len(strs[0])
#     for col in range(0, n):
#         for row in range(1, m):
#             cur_word = strs[row]
#             pre_word = strs[row - 1]
#             if len(cur_word) <= col or len(pre_word) <= col or cur_word[col] != pre_word[col]:
#                 return strs[0][0: col]
#     return strs[0]
# print(longestCommonPrefix(["flower","flow","flight"]))

#
# def isValid(s: str) -> bool:
#     stack = []
#     dic = {')': '(', ']': '[', '}': '{'}
#     for item in s:
#         if item == '(' or item == '[' or item == '{':
#             stack.append(item)
#         else:
#             if len(stack) > 0 and stack.pop() == dic[item]:
#                 continue
#             else:
#                 return False
#     if len(stack) == 0:
#         return True
# print(isValid("["))

# def searchInsert(nums: List[int], target: int) -> int:
#     len_nums = len(nums)
#     tmp = len_nums // 2
#     while tmp > 0 and tmp < len_nums:
#         if nums[tmp] == target:
#             return tmp
#         elif nums[tmp] > target:
#             tmp = tmp // 2
#         else:
#             tmp = (len_nums + tmp) // 2
#     return tmp
# print(searchInsert([1,3,5,6], 5))


# def lengthOfLastWord(s: str) -> int:
#     print(s.strip())  #fly me   to   the moon
#     print(s.split(' '))  #['', '', '', 'fly', 'me', '', '', 'to', '', '', 'the', 'moon', '', '']
#     print(s.strip().split(' '))  #['fly', 'me', '', '', 'to', '', '', 'the', 'moon']
#     print(s)  #   fly me   to   the moon
#     return s.strip().split(' ')[-1]  #moon
# print(lengthOfLastWord("   fly me   to   the moon  "))

# def plusOne(digits: List[int]) -> List[int]:
#     n = len(digits)
#     for i in range(n - 1, -1, -1):
#         if digits[i] != 9:
#             digits[i] += 1
#             for j in range(i + 1, n):
#                 digits[j] = 0
#             return digits
#
#     # digits 中所有的元素均为 9
#     return [1] + [0] * n
#
#
# print(plusOne([1, 2, 9, 2, 2, 9, 9]))

# def addBinary(a: str, b: str) -> str:
#     len_a = len(a)
#     len_b = len(b)
#     carry = 0
#     m, n = len_a-1, len_b-1
#     ans = ''
#     while m >= 0 or n >= 0 or carry > 0:
#         val = carry
#         if m >= 0:
#             val += int(a[m])
#             m -= 1
#         if n >= 0:
#             val += int(b[n])
#             n -= 1
#         carry = val // 2
#         val = val % 2
#         ans = str(val) + ans
#     return ans
#
# print(addBinary("1010", "1011"))

# def mySqrt(x: int) -> int:
#     left = 0
#     right = x
#     ans = 0
#     while left <= right:
#         mid = (right - left) // 2 + left
#         if mid ** 2 == x:
#             return mid
#         elif mid ** 2 > x:
#             ans = mid - 1
#             right =mid - 1
#         else:
#             left = mid + 1
#     return ans
# print(mySqrt(2147395599))

# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     p1 = m - 1
#     p2 = n - 1
#     t = m + n - 1
#     while p1 >= 0 and p2 >= 0:
#         if nums2[p2] >= nums1[p1]:
#             nums1[t] = nums2[p2]
#             p2 -= 1
#             t -= 1
#         else:
#             nums1[t] = nums1[p1]
#             p1 -= 1
#             t -= 1
#     while p2 >= 0:
#         nums1[t] = nums2[p2]
#         p2 -= 1
#         t -= 1
# # merge([0], 0, [1], 1)
# merge([2, 0], 1, [1], 1)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     # def preorder(self,root):
#     #     stack, ans = [root], []
#     #     while stack:
#     #         p = stack.pop()
#     #         if isinstance(p, TreeNode):
#     #             stack.extend([p.right, p.left, p.val])
#     #         elif isinstance(p, int):
#     #             ans.append(p)
#     #     return ans
#     ans = []
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return
#         self.inorderTraversal(root.left)
#         self.ans.append(root.val)
#         self.inorderTraversal(root.right)
#         return self.ans
#
#
# if __name__ == '__main__':
#     root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
#     s = Solution()
#     print(s.inorderTraversal(root))
#     # print(s.ans)
#     # print(s.preorder(root))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def preorder(root):
#             stack,ans = [root],[]
#             while stack:
#                 p = stack.pop()
#                 if isinstance(p, TreeNode):
#                     stack.extend([p.right, p.left, p.val])
#                 elif isinstance(p, int):
#                     ans.append(p)
#                 else:
#                     ans.append(None)
#             return ans
#         def postorder(root):
#             stack,ans = [root],[]
#             while stack:
#                 p = stack.pop()
#                 if isinstance(p, TreeNode):
#                     stack.extend([p.val, p.right, p.left])
#                 elif isinstance(p, int):
#                     ans.append(p)
#                 else:
#                     ans.append(None)
#             return ans
#         pre_ = preorder(root)
#         print(pre_)
#         post_ = postorder(root)
#         print(post_)
#
#         if pre_ == list(reversed(post_)):
#             return True
#         else:
#             return False
#
# if __name__ == '__main__':
#     # root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
#     # root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
#     root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
#     s = Solution()
#     print(s.isSymmetric(root))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     # 当前叶子节点的路径和
#     sum = 0
#     flag = False
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         self.traverse(root, targetSum)
#         return self.flag
#     def traverse(self, root, targetSum):
#         if not root:
#             return
#         self.sum += root.val
#         if not root.left and not root. right:
#             if self.sum == targetSum:
#                 self.flag = True
#         self.traverse(root.left, targetSum)
#         self.traverse(root.right, targetSum)
#         self.sum -= root.val
#
# if __name__ == '__main__':
#     root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
#     s = Solution()
#     print(s.hasPathSum(root, 22))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def __init__(self):
#         self.sum, self.ans = 0, False
#
#     def helper(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return
#         self.sum += root.val
#         if not root.left and not root.right:
#             self.ans = (self.sum == targetSum)
#         self.helper(root.left, targetSum)
#         self.helper(root.right, targetSum)
#         self.sum -= root.val
#
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         self.helper(root, targetSum)
#         return self.ans
#
# if __name__ == '__main__':
#     root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
#     s = Solution()
#     print(s.hasPathSum(root, 22))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     depth = 0
#     flag = True
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.traverse(root)
#         return self.flag
#     def traverse(self, root):
#         if not root:
#             return 0
#         self.depth += 1
#         left_depth = self.traverse(root.left)
#         right_depth = self.traverse(root.right)
#         res = abs(left_depth - right_depth)
#         if res > 1:
#             self.flag = False
#         self.depth -= 1
#         return self.depth
#
# if __name__ == '__main__':
#     root = TreeNode(1,TreeNode(2, TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))
#     s = Solution()
#     print(s.isBalanced(root))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         a = 0
#         left_height, right_height = 0, 0
#         b = [0]
#
#         def hepler(node):
#             print(a)
#             print(left_height)
#             b.append(123)
#             print(b)
#             # if not node.left and not node.right:
#             #     return abs(left_height - right_height) <= 1
#             # if node.left:
#             #     left_height += 1
#             # if node.right:
#             #     right_height += 1
#             # hepler(node.left)
#             # hepler(node.right)
#             # left_height -= 1
#             # right_height -= 1
#
#         return hepler(root)
# if __name__ == '__main__':
#     root = TreeNode(1,TreeNode(2, TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))
#     s = Solution()
#     print(s.isBalanced(root))
#
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.list = [float('-inf'), float('inf')]
#         self.depth = 0
#
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#
#         def helper(node):
#             if not node:
#                 return 0
#             self.depth += 1
#             if not node.left or not node.right:
#                 self.list[0] = max(self.list[0], self.depth)
#                 self.list[1] = min(self.list[1], self.depth)
#             helper(node.left)
#             helper(node.right)
#             self.depth -= 1
#         helper(root)
#         return self.list[0] - self.list[1] <= 1
#
# if __name__ == '__main__':
#     # root = TreeNode(1,None,TreeNode(2, None, TreeNode(3)))
#     root = TreeNode(1, TreeNode(2,TreeNode(4,TreeNode(8)),TreeNode(5)), TreeNode(3,TreeNode(6)))
#     s = Solution()
#     print(s.isBalanced(root))


# arr = [40,11,26,26,-20]
# # dic = {arr[i]: i+1 for i in range(len(arr)) if arr[i] not in dic}
# # dic = {arr[i]: i+1 for i in range(len(arr)) if i not in arr}
#
# dic = {val:len(arr)-i for i, val in enumerate(arr[::-1])}
#
# print(dic)

# import pandas as pd
#
# df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# print(df)
# #    A  B
# # 0  1  3
# # 1  2  4
# for column in df:
#     print(df[column])
# # 0    1
# # 1    2
# # Name: A, dtype: int64
# # 0    3
# # 1    4
# # Name: B, dtype: int64

# import pandas as pd
#
# df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
#
# for index, row in df.iterrows():
#     print(row['A'], row['B'])
# # 1 3
# # 2 4

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         sum = 0
#         for i in str(n):
#             sum += 1*int(i)
#         return sum
# s = Solution()
# print(s.hammingWeight(int('00000000000000000000000000001011')))

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         set_a = set(i for i in range(0, n+1))
#         set_b = set(nums)
#         set_c = set_a - set_b
#         return list(set_c)[0]
# s = Solution()
# print(s.missingNumber([3,0,1]))

# str = 'abcdefg'
# list = [ord(i) if ord(i) > 98 else i for i in str]
# print(list)

# print(os.listdir('.'))  # ['123123.xlsx', 'read_merged_excel.py', '.DS_Store', 'out_file', 'file', 'test4.py', 'test0.py', 'test1.py', 'test5.py', 'AdvancedPython', 'test_LC.py', 'test1.py', 'test6.py', 'test7.py', 'test3.py', 'test8.py', 'main.py', 'result.xlsx', '.idea']
#
# print(os.listdir(b'.'))  # [b'123123.xlsx', b'read_merged_excel.py', b'.DS_Store', b'out_file', b'file', b'test4.py', b'test0.py', b'test1.py', b'test5.py', b'\xe9\xab\x98\xe7\xba\xa7python', b'test_LC.py', b'test1.py', b'test6.py', b'test7.py', b'test3.py', b'test8.py', b'main.py', b'result.xlsx', b'.idea']

# # 36-数独问题
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         hash_map = {(row, column): set() for column in range(3) for row in range(3)}
#
#         for index in range(9):
#             column_set = set()
#             row_set = set()
#
#             for column_index in range(9):
#                 if board[index][column_index] == '.':
#                     continue
#
#                 if board[index][column_index] in column_set:
#                     return False
#                 else:
#                     column_set.add(board[index][column_index])
#
#                 if board[index][column_index] not in hash_map[(index // 3, column_index // 3)]:
#                     hash_map[(index // 3, column_index // 3)].add(board[index][column_index])
#                 else:
#                     return False
#
#             for row_index in range(9):
#                 if board[row_index][index] == '.':
#                     continue
#
#                 if board[row_index][index] in row_set:
#                     return False
#                 else:
#                     row_set.add(board[row_index][index])
#         return True
#
# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
#
# s =Solution()
# print(s.isValidSudoku((board)))

# class RelationResource(Resource):
#     method_decorators = {'post': [login_required]}
#
#     def post(self):
#         parser_ = RequestParser()
#         parser_.add_argument('model_id', type=int, required=True)
#         parser_.add_argument('index_id_list', action='append', required=True)
#         args = parser_.parse_args()
#         user_id = current_user.id
#         model_id = args.model_id
#
#         object_ = ModeInfo.query.get(model_id)
#         if object_ is None:
#             return {'message': 'failure', 'errmsg': '当前模型不存在'}
#         if object_.user_id != user_id:
#             return {'message': 'failure', 'errmsg': '用户信息错误'}
#
#         index_id_list = [int(i) for i in args.index_id_list[0].split(',')]
#
#         data_list = []
#
#         # insert_sql_1：向MODELINDEX中插入数据
#         insert_sql_1 = text(
#             """
#             INSERT INTO MODELINDEX VALUES (:MODEL_ID,:INDEX_ID)
#             """
#         )
#
#         # select_sql_3：查询MODELINDEX, 根据 MODEL_ID 查询 INDEX_id
#         select_sql_3 = text(
#             """
#             SELECT INDEX_ID FROM MODELINDEX WHERE MODEL_ID=:MODEL_ID
#             """
#         )
#
#         # cte_sql_1：根据末级index_id查询指标树形结构   UNION ALL合并两个select语句的结果（不去重）
#         cte_sql_1 = text(
#             """
#             WITH T (ID,PARENT_ID,NAME) AS (
#             SELECT ID,PARENT_ID,NAME FROM INDEXINFO WHERE ID=:ID UNION ALL
#             SELECT D.ID,D.PARENT_ID,D.NAME FROM T,INDEXINFO D WHERE T.PARENT_ID=D.ID)
#             SELECT*FROM T
#             """
#         )
#
#         select_sql_1 = text(
#             """
#              SELECT
#                 WARNINFO.ID AS ID,
#                 WARNINFO.LEVELNAME AS LEVELNAME,
#                 WARNINFO.SIGN AS SIGN,
#                 WARNINFO.VALUE AS VALUE,
#                 WARNINFO.STANDARD AS STANDARD
#             FROM
#                 WARNINFO
#                 INNER JOIN INDEXINFO ON WARNINFO.INDEX_ID = INDEXINFO.ID
#             WHERE
#                 WARNINFO.INDEX_ID = :INDEX_ID
#                 AND WARNINFO.USER_ID = :USER_ID
#                 AND WARNINFO.MODEL_ID = :MODEL_ID
#             ORDER BY
#                 WARNINFO.ID ASC
#             """
#         )
#
#         # 根据index_id 查询INDEXBASEINFO表 innerjoin INDEXINFO表的信息
#         select_sql_2 = text(
#             """
#             SELECT
#                 *
#             FROM
#                 INDEXBASEINFO
#                 INNER JOIN INDEXINFO ON INDEXBASEINFO.INDEX_ID = INDEXINFO.ID
#             WHERE
#                 INDEXINFO.ID = :ID
#             """
#         )
#
#         delete_sql_1 = "DELETE FROM MODELINDEX WHERE MODELINDEX.MODEL_ID=:MODEL_ID AND MODELINDEX.INDEX_ID IN"
#
#         delete_sql_2 = "DELETE FROM WARNINFO WHERE WARNINFO.MODEL_ID=:MODEL_ID AND WARNINFO.USER_ID=:USER_ID AND WARNINFO.INDEX_ID IN"
#
#         result = db.session.execute(select_sql_3, {'MODEL_ID': model_id})
#         old_list = [i[0] for i in result]  # 模型本来就存在的指标
#         not_similar_list = [i for i in index_id_list if i not in old_list]  # not_similar_list，需要新增的指标，需要重新插入到数据库
#         delete_id_list = [i for i in old_list if i not in index_id_list]  # 需要删除的指标
#         similar_list = set(old_list) & set(index_id_list)  # similar_list，模型下的指标 和 本次选取的指标 求交集，不需要重新插入到数据库
#         if len(delete_id_list) != 0:
#             sql, param = SqlHandle.sql_in(delete_sql_1, delete_id_list)
#             param.update({'MODEL_ID': model_id})
#             db.session.execute(text(sql), param)
#             sql, param = SqlHandle.sql_in(delete_sql_2, delete_id_list)
#             param.update({'MODEL_ID': model_id, 'USER_ID': user_id})
#             db.session.execute(sql, param)
#
#         try:
#             sort_list = []
#             for index_id in similar_list:  # similar_list，模型下的指标 和 本次选取的指标 求交集，不需要重新插入到数据库
#                 result_1 = db.session.execute(cte_sql_1, {'ID': index_id})
#                 result_1 = result_1.fetchall()
#                 result_2 = db.session.execute(select_sql_2, {'ID': index_id})
#                 result_2 = result_2.fetchall()
#                 sort_list.append(str(result_1[0][0]))  # result_1[0][0] 末级指标的index_id   result_1：[(1601, 1600, '毛利率异常'), (1600, 1599, '经营'), (1599, 1598, '企业经营'), (1598, None, '财务调整项')]
#                 data_dict = {
#                     'id': result_1[0][0],
#                     'level1': result_1[3][2],  # 一级指标name '财务调整项'
#                     'level2': result_1[2][2],  # 二级指标name '企业经营'
#                     'level3': result_1[1][2],  # 三级指标name '经营'
#                     'level4': result_1[0][2],  # 四级指标name '毛利率异常'  末级指标
#                     'description': result_2[0][1],  # 末级指标描述 '成本、价格、毛利率等指标的绝对水平及趋势变化是否符合行业特征'
#                     'type': result_2[0][2],  # INDEXTYPE 3：关注项   2：否决项  1：预警项
#                     'sign': None,
#                     'warndata': []
#                 }
#                 result = db.session.execute(select_sql_1, {'INDEX_ID': result_1[0][0], 'USER_ID': user_id, 'MODEL_ID': model_id})
#                 for i in result:
#                     data_dict.update({'sign': i[2]})
#                     data_dict_1 = {'warnname': i[1], 'sign': i[2], 'value': i[3], 'standard': i[4]}
#                     data_dict['warndata'].append(data_dict_1)
#                 data_list.append(data_dict)
#
#             for index_id in not_similar_list:  # not_similar_list，需要新增的指标，需要重新插入到数据库
#                 result_1 = db.session.execute(cte_sql_1, {'ID': index_id})
#                 result_1 = result_1.fetchall()
#                 result_2 = db.session.execute(select_sql_2, {'ID': index_id})
#                 result_2 = result_2.fetchall()
#                 sort_list.append(str(result_1[0][0]))
#                 data_dict = {
#                     'id': result_1[0][0],
#                     'level1': result_1[3][2],
#                     'level2': result_1[2][2],
#                     'level3': result_1[1][2],
#                     'level4': result_1[0][2],
#                     'description': result_2[0][1],
#                     'type': result_2[0][2],
#                     'sign': None,
#                     'warndata': []
#                 }
#                 result = db.session.execute(select_sql_1, {'INDEX_ID': result_1[0][0], 'USER_ID': user_id, 'MODEL_ID': model_id})
#                 for i in result:
#                     data_dict.update({'sign': i[2]})
#                     data_dict_1 = {'warnname': i[1], 'sign': i[2], 'value': i[3], 'standard': i[4]}
#                     data_dict['warndata'].append(data_dict_1)
#                 data_list.append(data_dict)
#                 db.session.execute(insert_sql_1, {'MODEL_ID': model_id, 'INDEX_ID': index_id})
#             db.session.commit()
#         except Exception as e:
#             current_app.logger.error(e)
#             db.session.rollback()
#             return {'message': 'failure', 'error': '添加指标出错'}
#         data_list = sorted(data_list, key=operator.itemgetter('id'))
#         return {'message': 'ok', 'model_id': model_id, 'data': data_list}

# nums = [3, 2, 3, 4, 4, 4, 4]
# c = Counter(nums)
# print(c.most_common())
# print(c.most_common(1)[0][0])

# # 206.反转链表
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
#         ans = None
#         ans = ListNode(None)
#
#         def helper(head):
#             nonlocal ans
#             if not head:
#                 return
#             tmp = head.next
#             head.next = ans
#             ans = head
#             helper(tmp)
#
#         helper(head)
#         return ans

# s = Solution()
# head_ = ListNode(1, ListNode(2))
# v = s.reverseList(head_)
# print(v.val, v.next.val)


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         p1 = head
#         p2 = head.next
#         while p2:
#             while p1.val == p2.val:
#                 p2 = p2.next
#             p1.next = p2
#             p1 = p1.next
#             p2 = p2.next
#         return head
#
# # [1,1,2,3,3,3,4]
# head = ListNode(1,ListNode(1, ListNode(2,ListNode(3,ListNode(3,ListNode(3,ListNode(4)))))))
# s = Solution()
# res = s.deleteDuplicates(head)
# print(res)

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         # c = dict(Counter(s))
#         c = Counter(s)
#         for i, item in enumerate(s):
#             if c[item] == 1:
#                 return i
#         return -1
# cls = Solution()
# s = "leetcode"
# print(cls.firstUniqChar(s))

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) < len(t):
#             return self.isAnagram(t, s)
#         c1 = Counter(s)
#         c2 = Counter(t)
#         c = c1 - c2
#         c_ = c2 - c1
#         if len(c) == 0:
#             return True
#         else:
#             return False
# cls = Solution()
# s = 'a'
# t = 'ab'
# print(cls.isAnagram(s, t))

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         queue = [root]
#         res = []
#         tmp = []
#         while queue:
#             item = queue.pop(0)
#             if isinstance(item, TreeNode):
#                 queue.extend([item.val, item.left, item.right])
#                 if not item.left and not item.right:
#                     res.append(tmp)
#                     tmp = []
#             elif isinstance(item, int):
#                 tmp.append(item)
#         if len(res[-1]) == 0:
#             res = res[:-1]
#         res.append(tmp)
#         return res
#
# s = Solution()
# root = TreeNode(1,TreeNode(2))
# print(s.levelOrder(root))

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         len1, len2 = len(word1), len(word2)
#         i, j =0,0
#         s = []
#         while i < len1 and j < len2:
#             s.append(word1[i])
#             s.append(word2[j])
#             i += 1
#             j += 1
#         if i < len1:
#             s.append(word1[i:])
#         if j < len2:
#             s.append(word2[j:])
#         res = ""
#         for i in s:
#             res += i
#         return res
#
#
# word1 = "abc"
# word2 = "pqr"
# s = Solution()
# print(s.mergeAlternately(word1, word2))




