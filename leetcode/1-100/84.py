class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		heights.append(0)
		n = len(heights)
		if n < 1:
			return 0
		stack = []
		prev = [0]*n
		best = 0
		for i in range(n):
			v = heights[i]
			j = i
			while len(stack) > 0 and heights[stack[-1]] > v:
				j = stack.pop()
				best = max(best, (i-j+prev[j])*heights[j])
			stack.append(i)
			prev[i] = i-j+prev[j]
		return best
