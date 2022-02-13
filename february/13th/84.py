from math import inf
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_ = -inf

    for height in heights:
        pops = 1
        while stack and stack[-1][0] > height:
            val, count = stack.pop()
            max_ = max(max_, val * (count + pops - 1))
            pops += count

        stack.append((height, pops))

    height = -1

    pops = 1
    while stack and stack[-1][0] > height:
        val, count = stack.pop()
        max_ = max(max_, val * (count + pops - 1))
        pops += count

    return max_
