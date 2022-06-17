def solution():
    n = int(input())

    for _ in range(n):
        a, b, c, x, y = [int(num) for num in input().split(' ')]
        print("NO" if max(0, x - a) + max(0, y - b) - c > 0 else "YES")


solution()
