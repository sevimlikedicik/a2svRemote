def solution():
    n = int(input())

    for _ in range(n):
        m = input()
        inputs = [int(num) for num in input().split(' ')]
        max_ = 0
        result = []
        for i in range(len(inputs) - 1, -1, -1):
            max_ = max(inputs[i], max_)
            result.append('1' if max_ > 0 else '0')
            max_ -= 1
        print(' '.join(list(reversed(result))))


solution()
