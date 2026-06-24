class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            while (r - l + 1) - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res