class Solution:
	def trap(self, height: List[int]) -> int:
		l, r = 0, len(height) - 1
		maxl, maxr = 0, 0
		water = 0
		while l <= r:
			waterh = min(maxl, maxr)
			if maxl <= maxr:
				h = height[l]
				maxl = max(maxl, h)
				l += 1
			else:
				h = height[r]
				maxr = max(maxr, h)
				r -= 1
			if waterh > h:
				water += waterh - h
		return water
