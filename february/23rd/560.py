from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    pre_sum = [0]
    pre_map = {0: 1}
    for i in range(len(nums)):
        sub_sum = pre_sum[i] + nums[i]
        pre_sum.append(sub_sum)
        if sub_sum not in pre_map:
            pre_map[sub_sum] = 0
        pre_map[sub_sum] += 1

    count = 0

    for i, pre_sum in enumerate(pre_sum):
        print(pre_map)
        if k - pre_sum in pre_map:
            count += pre_map[k - pre_sum]
        pre_map[pre_sum] -= 1
        if pre_map[pre_sum] == 0:
            del pre_map[pre_sum]

    return count
