import math
class Solution:
	def maxArea(self, height: List[int]) -> int:
		l = 0
		r = len(height) - 1
		max_area = 0
		while l < r:
			w = r - l
			if height[l] < height[r]:
				h = height[l]
				l = l + 1
			else:
				h = height[r]
				r = r - 1
			max_area = max(max_area, h*w)
		return max_area
