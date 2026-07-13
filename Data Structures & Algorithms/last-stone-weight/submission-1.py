class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s for s in stones]
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if second < first:
                heapq.heappush_max(stones, first - second)
        
        return stones[0] if stones else 0
