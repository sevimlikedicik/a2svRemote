from math import inf
from typing import List


def maxProfit(prices: List[int]) -> int:
    max_diff = 0
    min_ = inf

    for price in prices:
        max_diff = max(max_diff, price - min_)
        min_ = min(min_, price)

    return max_diff
