from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        num = int(input())
        if num % 2 == 1:
            print(-1)
        else:
            print(num // 2, num // 2, 0)


solution()
