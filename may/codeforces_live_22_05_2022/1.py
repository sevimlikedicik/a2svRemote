def solution():
    n = int(input())

    for _ in range(n):
        m = input()
        s = input()
        mid = (len(s) - 1) // 2
        walk = mid + 1
        count = 0 if len(s) % 2 == 0 else 1
        while walk < len(s) and s[walk] == s[mid]:
            count += 2
            walk += 1
            # print(count, walk)

        print(count)


solution()
