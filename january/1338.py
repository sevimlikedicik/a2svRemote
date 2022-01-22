from typing import List


def minSetSize(arr: List[int]) -> int:
    nums = {}
    for num in arr:
        if num not in nums:
            nums[num] = 0

        nums[num] += 1

    total = 0
    for i, count in enumerate(sorted(nums.values(), reverse=True)):
        total += count
        if total >= len(arr) // 2:
            return i + 1
