class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i!= 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            val = -1 * nums[i]
            while j < k:
                s = nums[j] + nums[k]
                if s > val:
                    k -= 1
                elif s < val:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res