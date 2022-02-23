from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # flag => last step increased (-1 is undefined)
        flag, size, max_ = -1, 1, 1

        for i in range(1, len(arr)):
            if flag == -1 and arr[i] != arr[i - 1]:
                flag = 1 if arr[i] > arr[i - 1] else 0
                size += 1
            elif (arr[i] > arr[i - 1] and flag == 0) or (arr[i] < arr[i - 1] and flag == 1):
                flag = 0 if flag == 1 else 1
                size += 1
            elif arr[i] == arr[i - 1]:
                size = 1
                flag = -1
            else:
                size = 2
            max_ = max(max_, size)

        return max_
