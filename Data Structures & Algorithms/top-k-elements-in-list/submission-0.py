class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        # create buckets where each position corresponds to a freq
        freq = [[] for i in range(len(nums) + 1 )]

        for n in nums:
            # current count of current n
            count[n] = 1 + count.get(n, 0)
        
        # append num value to count frequency key 
        # value n occurs c number of times
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        # descending order starting from biggest num which is highest count
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
