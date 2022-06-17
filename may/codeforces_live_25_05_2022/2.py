def solution():
    n = int(input())

    for _ in range(n):
        a_count = int(input())
        nums = [int(num) for num in input().split(' ')]
        count = 0
        i = 0
        while i < (len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                i += 1
            i += 1

        print(count)


solution()
