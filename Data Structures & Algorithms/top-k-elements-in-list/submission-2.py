class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        res = []
        bucketArr = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        for item, freq in freqMap.items():
            bucketArr[freq].append(item)
        for i in range(len(nums), 0, -1):
            res.extend(bucketArr[i])
            if len(res) == k:
                return res