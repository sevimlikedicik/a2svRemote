from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    if k == 0:
        return False
    setto = set(nums[0:k])
    if k > len(nums):
        return len(setto) < len(nums)

    if len(setto) < k:
        return True

    for i in range(k, len(nums)):
        if nums[i] in setto:
            return True
        setto.remove(nums[i - k])
        setto.add(nums[i])

    return False
