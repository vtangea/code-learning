class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        merged = []
        for i in sorted(intervals, key=lambda e: (e.start)):
            if merged and i.start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, i.end)
            else:
                merged.append(i)
        return merged
