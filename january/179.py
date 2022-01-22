from typing import List


class MyNumber:
    def __init__(self, value):
        self.value = str(value)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return f"{self.value}{other.value}" > f"{other.value}{self.value}"

    def __repr__(self):
        return self.value


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted([MyNumber(num) for num in nums], reverse=True)
        return str(int("".join([num.value for num in nums])))


sln = Solution()
print(sln.largestNumber([0, 0]))
