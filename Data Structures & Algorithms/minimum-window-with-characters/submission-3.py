class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len (s):
            return ""
        tFreq = Counter(t)
        l = 0
        window = {}
        have, need = 0, len(tFreq)
        res, resLen = [-1, -1], float("+inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tFreq and tFreq[c] == window[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r+1] if resLen != float("+inf") else ""

