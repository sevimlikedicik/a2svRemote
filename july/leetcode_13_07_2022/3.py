from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        size = int(input())
        nums = [int(num) for num in input().split(' ')]
        indexes = [0 for _ in range(size)]
        for i, num in enumerate(nums):
            indexes[num] = i

        left, right, possible_seats, res = indexes[0], indexes[0], 0, 1

        for i in range(1, size):
            index = indexes[i]
            if index < left:
                possible_seats += left - index - 1
                left = index
            elif index > right:
                possible_seats += index - right - 1
                right = index
            else:
                res *= possible_seats
                res = res % 1000000007
                possible_seats -= 1

        print(res)


solution()
