def solution():
    n = int(input())
    arr = [int(num) for num in input().split(' ')]
    one_count = [0, False]
    two_count = [0, False]
    best = 0

    for num in arr:
        if num == 1:
            if one_count[1]:
                one_count[0] += 1
            else:
                one_count[0] = 1
                one_count[1] = True
                two_count[1] = False
        else:
            if two_count[1]:
                two_count[0] += 1
            else:
                two_count[0] = 1
                two_count[1] = True
                one_count[1] = False
        best = max(best, min(one_count[0], two_count[0]) * 2)

    print(best)


solution()
