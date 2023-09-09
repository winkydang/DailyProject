from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 定义差分数组，元素初始化为0
        diff = [0] * n

        for left, right, inc in bookings:
            diff[left - 1] += inc

            if right - 1 + 1 < n:
                diff[right - 1 + 1] -= inc

        # 对差分数组求前缀和即可得到原数组
        for i in range(1, n):
            diff[i] = diff[i] + diff[i - 1]

        return diff


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5

cls = Solution()
res = cls.corpFlightBookings(bookings, n)
print(res)
