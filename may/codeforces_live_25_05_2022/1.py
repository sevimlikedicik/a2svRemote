def solve(nums):
    sum_ = sum(nums)
    for num in nums:
        if num == sum_ / len(nums):
            return True

    return False


def solution():
    n = int(input())

    for _ in range(n):
        a_count = int(input())
        nums = [int(num) for num in input().split(' ')]
        if solve(nums):
            print("YES")
        else:
            print("NO")


solution()
