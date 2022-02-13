from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    pos = {}
    for i, num in enumerate(nums2):
        pos[num] = i

    res = []
    for num in nums1:
        greater_found = False
        for i in range(pos[num] + 1, len(nums2)):
            if num < nums2[i]:
                res.append(nums2[i])
                greater_found = True
                break

        if not greater_found:
            res.append(-1)

    return res
