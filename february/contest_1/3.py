def get_beecola(cash, shops):
    low, high, out = 0, len(shops) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        if shops[mid] > cash:
            high = mid - 1
        else:
            low = mid + 1
            out = low
    return out


def solution():
    n = int(input())
    shops = [int(num) for num in input().split(' ')]
    day_count = int(input())
    shops = sorted(shops)
    for i in range(0, day_count):
        cash = int(input())
        print(get_beecola(cash, shops))


solution()
