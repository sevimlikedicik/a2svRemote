from math import inf
from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    left = 0
    right = k - 1
    sub_sum = sum(nums[0:k])
    max_ = -inf

    while right < len(nums) - 1:
        max_ = max(max_, sub_sum)
        sub_sum -= nums[left]
        left += 1
        right += 1
        sub_sum += nums[right]

    max_ = max(max_, sub_sum)

    return max_ / k
