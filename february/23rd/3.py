class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_ = 0, 0, 0
        chars = set()

        while right < len(s):
            if s[right] in chars:
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                left += 1

            chars.add(s[right])
            max_ = max(max_, right - left + 1)
            right += 1

        return max_
