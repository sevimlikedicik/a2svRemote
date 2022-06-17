def solution():
    n = int(input())

    for _ in range(n):
        size = int(input())
        nums = [int(num) for num in input().split(' ')]
        if size % 2 == 1:
            print("NO")
            continue

        cond = True
        nums.sort()
        new_arr = [0 for _ in range(size)]
        for i in range(0, size, 2):
            new_arr[i] = nums[i // 2]

        j = 0
        for i in range(size // 2, size - 1, 1):
            if nums[i] <= new_arr[j] or nums[i] <= new_arr[j + 2]:
                cond = False
                break
            else:
                new_arr[j + 1] = nums[i]
                j += 2

        if not cond:
            print("NO")
        else:
            if nums[-1] > new_arr[j]:
                new_arr[j + 1] = nums[-1]
                new_arr = [str(num) for num in new_arr]
                print("YES")
                print(' '.join(new_arr))
            else:
                print("NO")


solution()
