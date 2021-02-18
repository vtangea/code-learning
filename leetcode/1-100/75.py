class Solution:
	def sortColors(self, nums: List[int]) -> None:
		def swap(i, j):
			tmp = nums[i]
			nums[i] = nums[j]
			nums[j] = tmp
		p1 = 0
		p2 = len(nums) - 1
		while p1 < p2:
			if nums[p1] == 0:
				p1 = p1 + 1
			else:
				swap(p1, p2)
				p2 = p2 - 1
		p2 = len(nums) - 1
		if nums[p1] == 0:
			p1 = p1 + 1
		while p1 < p2:
			if nums[p1] == 1:
				p1 = p1 + 1
			else:
				swap(p1, p2)
				p2 = p2 - 1
