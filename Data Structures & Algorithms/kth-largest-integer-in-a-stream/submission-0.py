class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minheap with k largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            # pop if len of min heap is greater than k elements
            heapq.heappop(self.minHeap)
        # min value always stored in 0 index for minheap
        return self.minHeap[0]
            
