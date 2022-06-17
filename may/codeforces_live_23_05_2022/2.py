def solution():
    n = int(input())

    for _ in range(n):
        a_count = int(input())
        cards = [int(num) for num in input().split(' ')]
        s_count = int(input())
        shuffles = [int(num) for num in input().split(' ')]
        print(cards[sum(shuffles) % a_count])


solution()
