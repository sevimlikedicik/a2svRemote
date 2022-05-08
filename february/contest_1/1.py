def solution():
    inputs = [int(num) for num in input().split(' ')]
    n = int(inputs[0])
    m = int(inputs[1])
    count = 0
    time_left = 240 - m
    for i in range(1, n + 1):
        if time_left - 5 * i < 0:
            break
        else:
            time_left -= 5 * i
            count += 1

    print(count)


solution()
