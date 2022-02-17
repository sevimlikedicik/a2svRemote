from typing import List


def largestAltitude(gain: List[int]) -> int:
    curr = 0
    max_ = 0
    for g in gain:
        curr += g
        max_ = max(curr, max_)

    return max_
