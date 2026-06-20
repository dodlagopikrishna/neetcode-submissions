class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        return True if sCount == tCount else False