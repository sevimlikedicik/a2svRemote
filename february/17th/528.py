import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.indexes = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.indexes, self.weights)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
