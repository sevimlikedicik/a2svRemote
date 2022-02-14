from typing import List


def pivotIndex(nums: List[int]) -> int:
    arr_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        if left_sum == (arr_sum - nums[i]) / 2:
            return i
        left_sum += nums[i]

    return -1
