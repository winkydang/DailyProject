# from collections import defaultdict
# from math import inf
#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         need, window = defaultdict(int), defaultdict(int)
#         for c in t:
#             need[c] += 1
#         left, right = 0, 0
#         valid_len = 0
#         start, len_tar = 0, inf  # 记录最小覆盖子串的起始索引及长度
#         while right < len(s):
#             tmp = s[right]  # 即将移入窗口的字符
#             right += 1  # 扩大窗口
#             # 进行窗口内数据的一系列更新
#             if tmp in need.keys():
#                 window[tmp] += 1
#                 if window[tmp] == need[tmp]:
#                     valid_len += 1
#
#             # 判断左侧窗口是否要收缩
#             while valid_len == len(need):
#                 if right - left < len_tar:  # 在这里更新最小覆盖子串
#                     start = left
#                     len_tar = right - left
#
#                 tmp2 = s[left]  # tmp2是将移出窗口的字符
#                 left += 1  # 缩小窗口
#                 if tmp2 in need.keys():  # # 进行窗口内数据的一系列更新
#                     if window[tmp2] == need[tmp2]:
#                         valid_len -= 1
#                     window[tmp2] -= 1
#
#         return "" if len_tar == inf else s[start:start + len_tar]
#
#
# cls = Solution()
# s = "aaaaaaaaaaaabbbbbcdd"
# t = "abcdd"
# print(cls.minWindow(s, t))
#
