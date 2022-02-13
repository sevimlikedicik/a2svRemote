from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums = sorted(nums)
    res = set()

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        pivot = nums[i]

        while left < right:
            sum_ = nums[left] + nums[right] + pivot
            if sum_ == 0:
                res.add((pivot, nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum_ > 0:
                right -= 1
            else:
                left += 1

    return res
