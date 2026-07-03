class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #initialize min heap
        # make stones negative
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # get largest stone
            first = heapq.heappop(stones)
            # get second largest stone
            second = heapq.heappop(stones)
            # keep in mind the nums are neg now (x < y)
            if second > first: 
                # add to heap
                heapq.heappush(stones, first - second)
        
        # if no more stones append 0 to return 0
        stones.append(0)

        # return abs value to get positive value
        return abs(stones[0])

        # while len(stones) > 1:
        ## sort stones at each pass
        #     stones.sort()
        #     cur = stones.pop() - stones.pop()
        ## if diff > 0, insert new stone back into list
        #     if cur:
        #         stones.append(cur)
        ## if list is empty return 0, else return remaining stone
        # return stones[0] if stones else 0