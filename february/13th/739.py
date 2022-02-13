from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0 for temp in temperatures]
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            val, ind = stack.pop()
            res[ind] = i - ind

        stack.append((temp, i))

    return res
