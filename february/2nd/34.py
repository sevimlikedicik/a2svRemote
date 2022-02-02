from typing import List


def get_edge(nums, target, left):
    if not nums:
        return -1

    low = 0
    high = len(nums) - 1
    border = low if left else high

    while low <= high:
        mid = (low + high) // 2
        # print(low, mid, high, left)
        edge_index = mid + 1 if left else mid - 1
        if mid == border and nums[mid] == target:
            return mid
        elif nums[mid] != target and (0 <= edge_index < len(nums) and nums[edge_index] == target):
            return edge_index
        elif nums[mid] == target:
            if left:
                high = mid - 1
            else:
                low = mid + 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def searchRange(nums: List[int], target: int) -> List[int]:
    left_edge = get_edge(nums, target, True)
    right_edge = get_edge(nums, target, False)

    return [left_edge, right_edge]
