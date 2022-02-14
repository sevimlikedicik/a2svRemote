from typing import List


def sumOddLengthSubarrays(arr: List[int]) -> int:
    run_sum = [0]

    for i in range(1, len(arr) + 1):
        run_sum.append(run_sum[i - 1] + arr[i - 1])

    sum_ = 0
    for i in range(1, len(run_sum), 2):
        for j in range(i, len(run_sum)):
            sum_ += run_sum[j] - run_sum[j - i]

    return sum_
