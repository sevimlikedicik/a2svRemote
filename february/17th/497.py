import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sizes = self.get_sizes()
        self.indexes = [i for i in range(len(rects))]

    def get_sizes(self):
        return [(rect[3] - rect[1] + 1) * (rect[2] - rect[0] + 1) for rect in self.rects]

    def pick(self) -> List[int]:
        chosen = self.rects[random.choices(self.indexes, self.sizes)[0]]
        return [random.randint(chosen[0], chosen[2]), random.randint(chosen[1], chosen[3])]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
