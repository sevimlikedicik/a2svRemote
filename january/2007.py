from typing import List


def findOriginalArray(changed: List[int]) -> List[int]:
    nums = {}

    for num in changed:
        if num not in nums:
            nums[num] = 0

        nums[num] += 1

    og_array = []

    if 0 in nums:
        if nums[0] % 2 == 1:
            return []
        else:
            og_array = [0 for _ in range(nums[0] // 2)]
            nums[0] = 0

    for num in sorted(nums.keys()):
        if nums[num] != 0:
            if num * 2 not in nums:
                return []
            else:
                nums[num * 2] -= nums[num]
                og_array += [num for _ in range(nums[num])]
                nums[num] = 0

    return og_array
