from math import inf
from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i - 1] + nums[i])

    min_so_far = inf
    max_subarray = -inf

    for sum_ in prefix_sum:
        max_subarray = max(max_subarray, sum_ - min_so_far)
        min_so_far = min(min_so_far, sum_)

    max_so_far = -inf
    min_subarray = inf

    for sum_ in prefix_sum:
        min_subarray = min(min_subarray, sum_ - max_so_far)
        max_so_far = max(max_so_far, sum_)

    return max(sum(nums) - min_subarray, max_subarray, sum(nums))
