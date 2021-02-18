class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) < 3):
            return []
        nums.sort()
        sol = []
        exist = {}
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            if (nums[i]) > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while (k > j):
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    if (str(nums[i]) + str(nums[j]) + str(nums[k]) not in exist):
                        sol.append([nums[i], nums[j], nums[k]])
                        exist[str(nums[i]) + str(nums[j]) + str(nums[k])] = True
                    j += 1
                    k -= 1
                else:
                    k -= 1
        return sol
