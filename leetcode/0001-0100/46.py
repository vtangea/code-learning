class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        def permuteHelper(start):
            if start == n:
                out.append(list(nums))
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                permuteHelper(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        permuteHelper(0)
        return out
