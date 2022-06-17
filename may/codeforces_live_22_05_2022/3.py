def solution():
    n = int(input())

    for _ in range(n):
        m = int(input())
        nums = [int(num) for num in input().split(' ')]
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        common = -1
        for k, v in counter.items():
            if v == 1:
                common = k

        if common != -1:
            nums.remove(common)

        nums.sort()
        min_a, min_b = 0, 0
        count_a, count_b = 1 if common != -1 else 0, 1 if common != -1 else 0

        for num in nums:
            if count_a < count_b:
                if num > min_a:
                    min_a = num
                    count_a += 1
                elif num > min_b:
                    min_b = num
                    count_b += 1
            else:
                if num > min_b:
                    min_b = num
                    count_b += 1
                elif num > min_a:
                    min_a = num
                    count_a += 1

        print(min(count_a, count_b))


solution()
