from typing import List


def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    total_time = 0
    tours = tickets[k]
    for _ in range(tours):
        for i in range(len(tickets)):
            if i == k and tickets[i] == 1:
                return total_time + 1
            if tickets[i] > 0:
                total_time += 1
                tickets[i] -= 1
