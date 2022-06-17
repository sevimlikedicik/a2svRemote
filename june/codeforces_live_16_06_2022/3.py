def solve(arr):
    total = 0
    last_index = 0
    for i in range(len(arr)):
        total += arr[i]
        if total == 0:
            last_index = i
            break
        if total < 0:
            return False

    for i in range(last_index + 1, len(arr)):
        if arr[i] != 0:
            return False

    return total == 0


def solution():
    n = int(input())

    for _ in range(n):
        size = int(input())
        nums = [int(num) for num in input().split(' ')]
        print("Yes" if solve(nums) else "No")


solution()
