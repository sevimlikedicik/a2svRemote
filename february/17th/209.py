from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    pre_sum = [0]

    for i in range(len(nums)):
        pre_sum.append(pre_sum[i] + nums[i])
    left = 0
    right = 0
    min_len = len(nums) + 1

    while right < len(pre_sum):
        sub_sum = pre_sum[right] - pre_sum[left]
        if sub_sum >= target:
            min_len = min(min_len, right - left)
            left += 1
        else:
            right += 1

    return 0 if min_len == len(nums) + 1 else min_len
