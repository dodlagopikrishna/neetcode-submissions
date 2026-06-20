class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashMap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]
        for val in hashMap.values():
            res.append(val)
        return res