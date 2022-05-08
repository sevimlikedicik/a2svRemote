import math


def solution():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        sqrt = math.sqrt(num)
        pairs = [
            [math.floor(sqrt), math.floor(sqrt)],
            [math.floor(sqrt), math.ceil(sqrt)],
            [math.ceil(sqrt), math.ceil(sqrt)],
        ]
        min_ = math.inf
        for pair in pairs:
            if pair[0] * pair[1] >= num:
                min_ = min(min_, pair[0] + pair[1] - 2)

        print(min_)


solution()
