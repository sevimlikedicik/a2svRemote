from math import inf
from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    for i in range(len(nums)):
        num = nums[i]
        while 0 < num <= len(nums):
            if i == num - 1:
                nums[i] = inf
                break
            temp = nums[num - 1]
            nums[num - 1] = inf
            num = temp

    for i, num in enumerate(nums):
        if num != inf:
            return i + 1

    return len(nums) + 1
