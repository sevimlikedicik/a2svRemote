from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        n, m = [int(num) for num in input().split(' ')]
        mtr = []
        for i in range(n):
            if i % 4 == 0 or i % 4 == 3:
                arr = []
                for j in range(m // 2):
                    if j % 2 == 0:
                        arr.append("1")
                        arr.append("0")
                    else:
                        arr.append("0")
                        arr.append("1")
                mtr.append(arr)
            else:
                arr = []
                for j in range(m // 2):
                    if j % 2 == 0:
                        arr.append("0")
                        arr.append("1")
                    else:
                        arr.append("1")
                        arr.append("0")
                mtr.append(arr)
        for arr in mtr:
            print(' '.join(arr))


solution()
