class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		out = []
		i = 0
		n = len(intervals)
		while i < n:
			if newInterval[0] <= intervals[i][1]:
				break
			out.append(intervals[i])
			i += 1
		if i >= n:
			return intervals + [newInterval]
		if newInterval[1] < intervals[i][0]:
			return out + [newInterval] + intervals[i:]
		start = min(intervals[i][0], newInterval[0])
		end = newInterval[1]
		while i < len(intervals)-1 and intervals[i+1][0] <= end:
			i += 1
		end = max(intervals[i][1], newInterval[1])
		out.append([start, end])
		out.extend(intervals[i+1:])
		return out
