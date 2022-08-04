from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        num = int(input())
        print(-1 if num % 2 == 1 else f"{num // 2} {num // 2} 0")


solution()
