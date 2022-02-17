from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    zero_count = 0
    product = 1

    for num in nums:
        if num == 0:
            zero_count += 1
            if zero_count > 1:
                return [0 for _ in range(len(nums))]
        else:
            product *= num

    res = []

    for num in nums:
        if zero_count > 0:
            if num != 0:
                res.append(0)
            else:
                res.append(product)
        else:
            res.append(product // num)

    return res
