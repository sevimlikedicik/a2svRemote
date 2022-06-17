from sys import stdin
input = stdin.readline

def dfs(children, ranges, index):
    if index not in children:
        return 1, ranges[index - 1][1]

    operations, child_sum = 0, 0
    for child in children[index]:
        operation, selected = dfs(children, ranges, child)
        operations += operation
        child_sum += selected

    if child_sum < ranges[index - 1][0]:
        return operations + 1, ranges[index - 1][1]
    elif child_sum > ranges[index - 1][1]:
        return operations, ranges[index - 1][1]

    return operations, child_sum


def solution():
    n = int(input())

    for _ in range(n):
        size = int(input())
        parents = [int(num) for num in input().split(' ')]
        ranges = []
        for i in range(size):
            left, right = [int(num) for num in input().split(' ')]
            ranges.append((left, right))
        children = {}
        for i, parent in enumerate(parents):
            index = i + 2
            if parent not in children:
                children[parent] = []
            children[parent].append(index)
        # print(children)
        print(dfs(children, ranges, 1)[0])


solution()