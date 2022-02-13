from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 1

    left = 1
    right = 0
    curr = nums[0]

    while right < len(nums):
        if nums[right] != curr:
            curr = nums[right]
            nums[left] = curr
            left += 1
        right += 1

    print(nums)
    return left
