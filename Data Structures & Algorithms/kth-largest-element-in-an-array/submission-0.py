class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k,len(nums)):
            heapq.heappush(min_heap,nums[i])
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
