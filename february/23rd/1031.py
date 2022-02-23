from typing import List


class Solution:
    def get_max_sum(self, nums, k):
        if k > len(nums):
            return 0
        sub_sum = 0

        for i in range(0, k):
            sub_sum += nums[i]

        max_ = sub_sum

        for i in range(k, len(nums)):
            sub_sum += nums[i]
            sub_sum -= nums[i - k]
            max_ = max(sub_sum, max_)

        return max_

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        sub_sum = 0
        for i in range(0, firstLen):
            sub_sum += nums[i]

        max_ = sub_sum + self.get_max_sum(nums[firstLen: len(nums)], secondLen)

        for i in range(firstLen, len(nums) - 1):
            sub_sum += nums[i]
            sub_sum -= nums[i - firstLen]
            other_best = max(self.get_max_sum(nums[0: i - firstLen + 1], secondLen),
                             self.get_max_sum(nums[i + 1: len(nums)], secondLen))
            max_ = max(max_, sub_sum + other_best)

        sub_sum += nums[-1]
        sub_sum -= nums[len(nums) - firstLen - 1]
        max_ = max(max_, sub_sum + self.get_max_sum(nums[0: len(nums) - firstLen], secondLen))

        return max_
