class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = (0, 1)
        for i in range(len(s) - 1):
            left = i
            right = i + 1
            while True:
                if left - 1 < 0 or right >= len(s) or s[left-1] != s[right]:
                    break
                left = left - 1
                right = right + 1
            if right - left > best[1] - best[0]:
                best = (left, right)
            left = i
            right = i + 2
            if s[left] != s[right-1]:
                continue
            while True:
                if left - 1 < 0 or right >= len(s) or s[left-1] != s[right]:
                    break
                left = left - 1
                right = right + 1
            if right - left > best[1] - best[0] and s[left] == s[right - 1]:
                best = (left, right)
        return s[best[0]:best[1]]
