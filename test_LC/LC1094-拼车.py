from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        res = [0] * 1001

        for num, left, right in trips:
            if max(res) > capacity:
                return False

            diff[0] = 0
            # 更新diff
            for i in range(1, right):
                diff[i] = res[i] - res[i-1]

            diff[left - 1] += num
            diff[right] -= num

            # 根据差分数组构造结果数组
            res[0] = diff[0]
            for i in range(1, right+1):
                res[i] = res[i-1] + diff[i]

        return True

cls = Solution()

trips = [[2,1,5],[3,3,7]]
capacity = 4

print(cls.carPooling(trips, capacity))


# from typing import List
# import heapq
#
#
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         # 最多有1001个车站
#         nums = [0] * 1001
#
#         # 构造差分解法
#         df = Difference(nums)
#
#         for val, i, j in trips:
#             df.increment(i, j, val)
#
#         res = df.result()
#
#         # 乘客自始自终都不应该超载
#         for i in range(len(res)):
#             if capacity < res[i]:
#                 return False
#         return True
#
#
# class Difference:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.diff = [0]*(len(nums)+1)
#
#
#     def increment(self, i, j, val):
#         self.diff[i] += val
#         self.diff[j+1] -= val
#
#
#     def result(self) ->List[int]:
#         res = [0] * len(self.nums)
#         res[0] = self.diff[0]
#         for i in range(1, len(self.nums)):
#             res[i] = res[i-1] + self.diff[i]
#         return res
#
# cls = Solution()
#
# trips = [[2,1,5],[3,3,7]]
# capacity = 4
#
# print(cls.carPooling(trips, capacity))
