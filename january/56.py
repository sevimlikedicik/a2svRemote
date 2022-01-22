from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda i: i[0])
    new_intervals = []

    for left, right in intervals:
        if new_intervals and left <= new_intervals[-1][1]:
            new_intervals[-1][1] = max(right, new_intervals[-1][1])
        else:
            new_intervals.append([left, right])

    return new_intervals
