# # 238. 除自身以外数组的乘积
# from typing import List
#
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         arr_1 =[]
#         arr_2 = []
#         arr_1.append(1)
#         for i in range(1, n+1):
#             arr_1.append(0)
#         for j in range(0, n):
#             arr_2.append(0)
#         arr_2.append(1)
#         for i in range(n):
#             arr_1[i+1] = arr_1[i]*nums[i]
#             arr_2[n-i-1] = arr_2[n-i]*nums[n-i-1]
#         res = []
#         for i in range(n):
#             res.append(arr_1[i]*arr_2[i+1])
#         return res
#
# c = Solution()
#
# print(c.productExceptSelf([1, 2, 3, 4]))
#
from typing import List


# 605 种花问题
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_n = len(flowerbed)
        i = 0
        while i < len_n:
            if flowerbed[i] == 1:
                i += 2
            elif i < len_n and flowerbed[i + 1] == 0:
                n -= 1
                i += 2
            elif i < len_n and flowerbed[i + 1] == 1:
                i += 3
        if n == 0:
            return True
        else:
            return False
s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1))

