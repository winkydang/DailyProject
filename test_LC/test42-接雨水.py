# # 一、暴力解法
# from typing import List
#
# def trap(height: List[int]) -> int:
#     n = len(height)
#     sum_ = 0
#     for item in range(1, n-1):
#         l_max, r_max = 0, 0
#         for i in range(0, item+1):
#             l_max = max(l_max, height[i])
#         for j in range(item, n):
#             r_max = max(r_max, height[j])
#         sum_ += min(l_max, r_max) - height[item]
#     return sum_
#
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height))

# 二、备忘录法










