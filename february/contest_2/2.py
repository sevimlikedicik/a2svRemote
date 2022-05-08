import bisect


def solution():
    inputs = [int(num) for num in input().split(' ')]
    n = int(inputs[0])
    m = int(inputs[1])
    students = [int(num) for num in input().split(' ')]
    students.sort()
    for _ in range(n):
        q = int(input())
        pos = bisect.bisect_left(students, q)
        if pos != 0 and pos < (m + 1) // 2:
            print("YES")
        else:
            print("NO")


solution()
