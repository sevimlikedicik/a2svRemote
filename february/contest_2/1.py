def solution():
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num <= 31:
            print(31)
        else:
            if num % 4 == 0:
                print(32)
            else:
                print(31)


solution()
