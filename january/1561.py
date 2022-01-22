from typing import List


def maxCoins(piles: List[int]) -> int:
    piles = sorted(piles)
    left = 0
    right = len(piles) - 1
    my_coins = 0

    while left < right:
        my_coins += piles[right - 1]
        right -= 2
        left += 1

    return my_coins
