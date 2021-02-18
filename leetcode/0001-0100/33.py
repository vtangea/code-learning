class Solution:
	def search(self, nums: List[int], target: int) -> int:
		def binSearch(l, r):
			if l > r:
				return -1
			if r - l <= 1:
				if target == nums[l]: return l
				elif target == nums[r]: return r
				else: return -1
			m = int((l + r)/2)
			if target == nums[m]:
				return m
			if nums[l] > nums[m-1]:
				if target >= nums[m+1] and target <= nums[r]:
					return binSearch(m+1, r)
				else:
					return binSearch(l, m-1)
			else:
				if target >= nums[l] and target <= nums[m-1]:
					return binSearch(l, m-1)
				else:
					return binSearch(m+1, r)
		return binSearch(0, len(nums)-1)
