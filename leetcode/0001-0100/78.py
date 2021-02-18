class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		out = []
		n = len(nums)
		def backtrack(base, start):
			out.append(base)
			for i in range(start, n):
				backtrack(base + [nums[i]], i+1)
		backtrack([], 0)
		return out
