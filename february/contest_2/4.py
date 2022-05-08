import bisect


def solution():
    inputs = [int(num) for num in input().split(' ')]
    n = int(inputs[0])
    m = int(inputs[1])
    assistants = []
    for _ in range(m):
        assistants.append([int(num) for num in input().split(' ')])

    assistants.sort()
    stack = [[0, assistants[0][0] - 1]]



solution()
