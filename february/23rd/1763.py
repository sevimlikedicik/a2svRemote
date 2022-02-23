class Solution:
    def check_nice(self, chars):
        lower_set = set([c.lower() for c in chars.keys()])
        return len(lower_set) * 2 == len(chars.keys())

    def longestNiceSubstring(self, s: str) -> str:
        max_ = ""
        for i in range(2, len(s) + 1):
            chars = {}
            for j in range(0, i):
                if s[j] not in chars:
                    chars[s[j]] = 0
                chars[s[j]] += 1

            if self.check_nice(chars):
                subs = s[0:i]
                if len(subs) > len(max_):
                    max_ = subs

            for j in range(i, len(s)):
                chars[s[j - i]] -= 1
                if chars[s[j - i]] == 0:
                    del chars[s[j - i]]

                if s[j] not in chars:
                    chars[s[j]] = 0
                chars[s[j]] += 1

                if self.check_nice(chars):
                    subs = s[j - i + 1:j + 1]
                    if len(subs) > len(max_):
                        max_ = subs

        return max_
