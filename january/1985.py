from typing import List


def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [int(num) for num in nums]
    return str(sorted(nums, reverse=True)[k - 1])
