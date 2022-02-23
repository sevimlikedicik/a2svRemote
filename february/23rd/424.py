class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0 for _ in range(26)]
        left, right, max_len = 0, 0, 0

        while right < len(s):
            chars[ord(s[right]) - ord("A")] += 1
            while sum(chars) - max(chars) > k:
                chars[ord(s[left]) - ord("A")] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
