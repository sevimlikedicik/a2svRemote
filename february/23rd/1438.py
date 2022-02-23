import bisect
from typing import List


def longestSubarray(nums: List[int], limit: int) -> int:
    prev_nums = []
    start, longest = 0, 0

    for num in nums:
        bisect.insort(prev_nums, num)
        size = prev_nums[len(prev_nums) - 1] - prev_nums[0]
        while size > limit:
            del prev_nums[bisect.bisect_left(prev_nums, nums[start])]
            start += 1
            size = prev_nums[len(prev_nums) - 1] - prev_nums[0]

        longest = max(longest, len(prev_nums))

    return longest
