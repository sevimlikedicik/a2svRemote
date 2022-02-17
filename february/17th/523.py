from typing import List


def checkSubarraySum(nums: List[int], k: int) -> bool:
    pre_sum = [0]
    for i in range(0, len(nums)):
        pre_sum.append((pre_sum[i] + nums[i]) % k)

    pos = {}
    for i in range(len(pre_sum)):
        x = pre_sum[i]
        if x in pos:
            if pos[x] != i - 1:
                return True
        else:
            pos[x] = i

    return False
