from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    left, right, max_, flipped = 0, 0, 0, 0

    while right < len(nums):
        if nums[right] == 0:
            if flipped == k:
                while nums[left] != 0:
                    left += 1
                left += 1
            else:
                flipped += 1

        max_ = max(max_, right - left + 1)
        right += 1

    return max_
