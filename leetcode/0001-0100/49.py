class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = {}
        for w in strs:
            s = ''.join(sorted(w))
            if s not in anags:
                anags[s] = []
            anags[s].append(w)
        ans = []
        for v in anags.values():
            ans.append(v)
        return ans
