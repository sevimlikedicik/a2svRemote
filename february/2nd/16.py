from math import inf
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    closest = inf

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ == target:
                return target
            if abs(sum_ - target) < abs(closest - target):
                closest = sum_

            if sum_ < target:
                left += 1
            else:
                right -= 1

    return closest
