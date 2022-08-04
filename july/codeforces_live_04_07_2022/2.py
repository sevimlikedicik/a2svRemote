from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        n, m = [int(num) for num in input().split(' ')]
        for i in range(n):
            line = []
            if i % 4 == 0 or i % 4 == 3:
                for j in range(m // 2):
                    line += ["1", "0"] if j % 2 == 0 else ["0", "1"]
            else:
                for j in range(m // 2):
                    line += ["0", "1"] if j % 2 == 0 else ["1", "0"]
            print(' '.join(line))


solution()
