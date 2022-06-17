def solution():
    n = int(input())

    for _ in range(n):
        s1, s2, s3 = [int(num) for num in input().split(' ')]
        a, a_i, a_counter = sorted(input()), 0, 0
        b, b_i, b_counter = sorted(input()), 0, 0
        c = ""

        while a_i < s1 and b_i < s2:
            if a_counter == s3:
                c += b[b_i]
                b_i += 1
                b_counter += 1
                a_counter = 0
                continue
            if b_counter == s3:
                c += a[a_i]
                a_i += 1
                a_counter += 1
                b_counter = 0
                continue
            if a[a_i] < b[b_i]:
                c += a[a_i]
                a_i += 1
                a_counter += 1
                b_counter = 0
            elif a[a_i] > b[b_i]:
                c += b[b_i]
                b_i += 1
                b_counter += 1
                a_counter = 0
            else:
                if a_counter < b_counter:
                    c += a[a_i]
                    a_i += 1
                    a_counter += 1
                    b_counter = 0
                else:
                    c += b[b_i]
                    b_i += 1
                    b_counter += 1
                    a_counter = 0

        print(c)


solution()
