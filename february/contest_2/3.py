import bisect


def solution():
    inputs = [int(num) for num in input().split(' ')]
    n = int(inputs[0])
    m = int(inputs[1])
    assistants = []
    for _ in range(m):
        assistants.append([int(num) for num in input().split(' ')])

    assistants.sort()
    max_right = assistants[0][1]
    for i in range(1, len(assistants)):
        if assistants[i][0] > max_right + 1:
            print("YES")
            return
        max_right = max(max_right, assistants[i][1])

    if max_right < n - 1 or assistants[0][0] > 0:
        print("YES")
        return

    print("NO")


solution()
