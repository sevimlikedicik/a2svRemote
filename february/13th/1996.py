from typing import List


def numberOfWeakCharacters(properties: List[List[int]]) -> int:
    props = sorted(properties, key=lambda x: (x[0], x[1]), reverse=True)
    strong = props[0]
    backup = props[0]
    weak_count = 0

    for prop in props:
        if prop[0] != backup[0]:
            strong = backup
        if prop[0] < strong[0] and prop[1] < strong[1]:
            weak_count += 1
        elif prop[1] > backup[1]:
            backup = prop

    return weak_count
