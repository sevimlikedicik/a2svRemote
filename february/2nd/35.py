from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    if target > nums[right]:
        return right + 1
    elif nums[left] < target <= nums[right]:
        return right

    return left
