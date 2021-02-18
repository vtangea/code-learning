class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = -float('inf')
        cur_max = cur_sum
        for n in nums:
            if n > cur_sum + n:
                cur_sum = n
            else:
                cur_sum = cur_sum + n
            cur_max = max(cur_sum, cur_max)
        return cur_max
