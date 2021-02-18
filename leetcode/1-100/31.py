import math
class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		L = len(nums)
		if L < 2:
			return
		x = L - 2
		while x >= 0 and nums[x] >= nums[x+1]:
			x = x - 1
		if x > -1:
			swap = nums[x]
			y = x
			while y + 1 < L and nums[y+1] > swap:
				y = y + 1
			nums[x] = nums[y]
			nums[y] = swap
		if x + 1 < L:
			for i in range(x+1, math.ceil(((x+1)+L)/2)):
				tmp = nums[i]
				swapi = L - (i - (x+1)) - 1
				nums[i] = nums[swapi]
				nums[swapi] = tmp
