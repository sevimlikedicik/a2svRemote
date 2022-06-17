def solution():
    n, m = [int(num) for num in input().split(' ')]
    mtr = []
    for _ in range(n):
        inputs = [int(num) for num in input().split(' ')]
        mtr.append(inputs)

    spotlight = 0
    for i in range(n):
        left = False
        for j in range(m):
            if mtr[i][j] == 1:
                left = True
                continue
            spotlight += 1 if left else 0
        right = False
        for j in range(m-1, -1, -1):
            if mtr[i][j] == 1:
                right = True
                continue
            spotlight += 1 if right else 0

    for i in range(m):
        top = False
        for j in range(n):
            if mtr[j][i] == 1:
                top = True
                continue
            spotlight += 1 if top else 0
        bottom = False
        for j in range(n-1, -1, -1):
            if mtr[j][i] == 1:
                bottom = True
                continue
            spotlight += 1 if bottom else 0

    print(spotlight)


solution()
