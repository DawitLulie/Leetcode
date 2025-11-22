class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        count_s = Counter(s)
        for c in t:
            if count_s.get(c, 0) == 0:
                return c
            count_s[c] -= 1
