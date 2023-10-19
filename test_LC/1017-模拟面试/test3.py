# 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。
#
# 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            # 将当前元素对应的索引处的元素变为负数
            index = abs(num) - 1
            if nums[index] < 0:
                # 如果已经是负数，说明之前已经访问过，加入结果列表
                result.append(index + 1)
            else:
                # 如果是正数，将其变为负数表示已访问过
                nums[index] = -nums[index]

        # 恢复数组，将所有元素恢复为正数
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return result

cls = Solution()
nums = [4,3,2,7,8,2,3,1]
res = cls.findDuplicates(nums)
print(res)

