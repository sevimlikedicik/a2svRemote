def solution():
    n = int(input())

    for _ in range(n):
        m = input()
        if len(m) == 2:
            print(m[1])
        else:
            print(min(m))


solution()
