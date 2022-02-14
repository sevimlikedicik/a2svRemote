from typing import List


def runningSum(nums: List[int]) -> List[int]:
    run_sum = [nums[0]]

    for i in range(1, len(nums)):
        run_sum.append(run_sum[i - 1] + nums[i])

    return run_sum
