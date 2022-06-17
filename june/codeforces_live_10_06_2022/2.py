def solution():
    n = int(input())

    for _ in range(n):
        a_count = int(input())
        nums = [int(num) for num in input().split(' ')]
        res = [0 for _ in range(a_count)]
        for i in range(1, a_count + 1):
            ind = 0
            while ind < a_count and (nums[ind] == i or res[ind] != 0):
                ind += 1
            # print(i, ind, res)
            if ind != a_count:
                res[ind] = i
        if res[a_count - 1] == 0:
            if a_count > 1:
                res[a_count - 1], res[a_count - 2] = res[a_count - 2], a_count
            else:
                print(-1)
                continue

        res = [str(x) for x in res]
        print(' '.join(res))


solution()
