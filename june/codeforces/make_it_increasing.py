def solution():
    n = int(input())

    for _ in range(n):
        size = int(input())
        nums = [int(num) for num in input().split(' ')]
        flag = False
        count = 0
        for i in range(size - 2, -1, -1):
            while nums[i] >= nums[i + 1] and nums[i] != 0:
                count += 1
                nums[i] //= 2
            if nums[i] == nums[i + 1] == 0:
                flag = True

        print(-1 if flag else count)


solution()
