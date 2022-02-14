from typing import List


def minStartValue(nums: List[int]) -> int:
    run_sum = [nums[0]]

    for i in range(1, len(nums)):
        run_sum.append(run_sum[i - 1] + nums[i])

    return -(min(run_sum)) + 1 if min(run_sum) < 0 else 1
