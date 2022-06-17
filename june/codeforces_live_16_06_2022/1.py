def solution():
    n = int(input())

    for _ in range(n):
        a, b = [int(num) for num in input().split(' ')]
        sol = ""
        if a > b:
            for i in range(b):
                sol += "01"
            for i in range(a-b):
                sol += "0"
        else:
            for i in range(a):
                sol += "10"
            for i in range(b-a):
                sol += "1"
        print(sol)

solution()
