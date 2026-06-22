class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            n = num
            if (n - 1) not in numSet:
                curLen = 1
                while (n+1) in numSet:
                    curLen +=1
                    n +=1
                longest = max(longest, curLen)
        return longest