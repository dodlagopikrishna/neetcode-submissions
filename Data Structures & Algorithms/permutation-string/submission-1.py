class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        hmap1 = {}
        hmap2 = {}

        for i in range(len(s1)):
            hmap1[s1[i]] = 1 + hmap1.get(s1[i], 0)
            hmap2[s2[i]] = 1 + hmap2.get(s2[i], 0)
        if hmap1 == hmap2:
            return True
        l, r = 0, len(s1)
        while r < len(s2):

            hmap2[s2[l]] -= 1
            if hmap2[s2[l]] == 0:
                del hmap2[s2[l]]
            hmap2[s2[r]] = 1 + hmap2.get(s2[r], 0)

            if hmap1 == hmap2:
                return True
            l += 1
            r += 1
        return False
