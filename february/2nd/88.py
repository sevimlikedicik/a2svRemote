from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1) - 1, len(nums2) - 1, -1):
        nums1[i] = nums1[i - len(nums2)]

    left = 0
    right = len(nums2)
    merger = 0

    while left < len(nums2) and right < len(nums1):
        if nums2[left] < nums1[right]:
            nums1[merger] = nums2[left]
            left += 1
        else:
            nums1[merger] = nums1[right]
            right += 1
        merger += 1

    if left < len(nums2):
        while left < len(nums2):
            nums1[merger] = nums2[left]
            left += 1
            merger += 1
