def solution():
    n = int(input())

    for _ in range(n):
        a_count = int(input())
        a_cards = [int(num) for num in input().split(' ')]
        b_count = int(input())
        b_cards = [int(num) for num in input().split(' ')]
        a_max = max(a_cards)
        b_max = max(b_cards)
        if a_max >= b_max:
            print("Alice")
        else:
            print("Bob")
        if b_max >= a_max:
            print("Bob")
        else:
            print("Alice")


solution()
