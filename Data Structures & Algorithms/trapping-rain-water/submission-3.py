class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l , r = 0, len(height) - 1
        water = 0
        while l < r:
            if height[l] < height[r]:
                curWater = maxL - height[l]
                maxL = max(maxL, height[l])
                l += 1
            else:
                curWater = maxR - height[r]
                maxR = max(maxR, height[r])
                r -= 1
            if curWater < 0:
                curWater = 0
            water += curWater
        return water