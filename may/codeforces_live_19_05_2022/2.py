def solution():
    n = int(input())

    for _ in range(n):
        inputs = [int(num) for num in input().split(' ')]
        print(f"{inputs[0] + inputs[1] + inputs[2]} {inputs[1] + inputs[2]} {inputs[2]}")


solution()
