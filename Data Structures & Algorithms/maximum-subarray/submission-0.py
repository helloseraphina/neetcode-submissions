class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]

        # constantly compute current sum
        curSum = 0

        for n in nums:
            # remove negative prefix from current sum
            # to ensure always computing max
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub