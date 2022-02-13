from math import inf
from typing import List


def maxSubArray(nums: List[int]) -> int:
    sums = [0]

    for i in range(1, len(nums) + 1):
        sums.append(sums[i - 1] + nums[i - 1])

    min_ = inf
    max_ = sums[1]

    for x in sums:
        max_ = max(x - min_, max_)
        min_ = min(x, min_)

    return max_
