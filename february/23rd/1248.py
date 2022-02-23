from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_positions = [-1]

        for i, num in enumerate(nums):
            if num % 2 == 1:
                odd_positions.append(i)

        odd_positions.append(len(nums))
        count = 0

        for i in range(k, len(odd_positions) - 1):
            count += (odd_positions[i + 1] - odd_positions[i]) * (odd_positions[i - k + 1] - odd_positions[i - k])

        return count
