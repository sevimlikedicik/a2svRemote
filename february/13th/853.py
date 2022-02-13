from math import inf
from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = []
    for i in range(len(position)):
        cars.append([position[i], speed[i]])
    cars = sorted(cars, key=lambda x: x[0])
    fleet_count = 0
    curr_fleet = [inf, inf]

    for i in range(len(cars) - 1, -1, -1):
        if cars[i][1] <= curr_fleet[1]:
            curr_fleet = cars[i]
            fleet_count += 1
        else:
            can_catch = float(target) >= cars[i][0] + cars[i][1] * (
                        (curr_fleet[0] - cars[i][0]) / (cars[i][1] - curr_fleet[1]))
            if not can_catch:
                curr_fleet = cars[i]
                fleet_count += 1
    return fleet_count
