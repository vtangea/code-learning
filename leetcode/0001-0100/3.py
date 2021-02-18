class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        start = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start = start + 1
            seen.add(s[i])
            if i + 1 - start > best:
                best = i + 1 - start
        return best
