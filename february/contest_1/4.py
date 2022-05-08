def total_damage(intervals, pre_sum, k):
    low, high, out = 0, len(intervals) - 1, 0

    while low <= high:
        mid = (low + high) // 2
        if intervals[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    return pre_sum[low] + (len(pre_sum) - low) * k


def bs(intervals, pre_sum, needed):
    low, high, out = 0, needed, 0

    while low <= high:
        mid = (low + high) // 2
        damage = total_damage(intervals, pre_sum, mid)
        if damage == needed:
            return mid
        elif damage < needed:
            low = mid + 1
            out = mid + 1
        else:
            high = mid - 1
    return out


def solution():
    n = int(input())
    for i in range(0, n):
        info = [int(num) for num in input().split(' ')]
        needed = info[1]
        attacks = [int(num) for num in input().split(' ')]
        intervals = [attacks[i] - attacks[i - 1] for i in range(1, len(attacks))]
        intervals.sort()
        pre_sum = [0]
        for j, interval in enumerate(intervals):
            pre_sum.append(pre_sum[j] + interval)
        print(bs(intervals, pre_sum, needed))


solution()
