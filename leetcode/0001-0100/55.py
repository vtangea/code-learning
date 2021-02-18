class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        while i >= 0:
            if nums[i] == 0:
                k = 0
                while True:
                    if i < 0:
                        return False
                    if nums[i] > k:
                        break
                    k += 1
                    i -= 1
            i -= 1
        return True
