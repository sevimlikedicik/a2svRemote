from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        n, m = [int(num) for num in input().split(' ')]
        print(min(min(n, m), (n+m) // 4))


solution()
