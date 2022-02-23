from math import inf


class Solution:
    def is_complete(self, og_map, curr_map):
        for key in og_map:
            if curr_map[key] < og_map[key]:
                return False

        return True

    def balancedString(self, s: str) -> int:
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

        items = list(counts.keys())
        for key in items:
            if counts[key] <= len(s) // 4:
                del counts[key]
            else:
                counts[key] = counts[key] - (len(s) // 4)

        left, right, min_size = 0, 0, inf
        curr_map = {}
        for key in counts:
            curr_map[key] = 0
        while right < len(s):
            c = s[right]
            if c in curr_map:
                curr_map[c] += 1
                while self.is_complete(counts, curr_map):
                    min_size = min(min_size, right - left + 1)
                    if s[left] in curr_map:
                        curr_map[s[left]] -= 1
                    left += 1
            right += 1

        return 0 if min_size == inf else min_size
