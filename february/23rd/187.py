from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        curr = s[0:10]
        pattern_map = {curr: 1}

        for i in range(10, len(s)):
            curr = curr[1:10] + s[i]
            if curr not in pattern_map:
                pattern_map[curr] = 0
            pattern_map[curr] += 1

        res = []
        for k, v in pattern_map.items():
            if v > 1:
                res.append(k)

        return res
