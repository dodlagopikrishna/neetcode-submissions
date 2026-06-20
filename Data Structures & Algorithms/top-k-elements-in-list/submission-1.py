class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        freqMap = Counter(nums)
        for key, val in freqMap.items():
            heapq.heappush(heap, (val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res