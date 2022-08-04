from sys import stdin

input = stdin.readline


def solution():
    positions = input()
    prev_pos = None
    prev_count = 0

    for c in positions:
        if c == prev_pos:
            prev_count += 1
        else:
            prev_pos = c
            prev_count = 1
        if prev_count >= 7:
            print("YES")
            return

    print("NO")
    return


solution()
