from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    uniques = {}

    for i, num in enumerate(nums):
        if target - num in uniques:
            return [i, uniques[target - num]]

        uniques[num] = i

    return []
