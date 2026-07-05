class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## BRUTE FORCE SOLUTION ##
        #init max water amount
        # max_water = 0

        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         # compute area
        #         # width * height
        #         area = (r - l) * min(heights[l], heights[r])
        #         max_water = max(max_water, area)
        
        # return max_water

        ## MORE EFFICIENT ##
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_water = max(max_water, area)
            
            # if height at l smaller, increment l pointer right to maximise heights
            if heights[l] < heights[r]:
                l += 1
            # if height at r smaller, increment left
            elif heights[r] < heights[l]:
                r -= 1
            # if heights equal, increment either l or r
            else:
                r -= 1

        return max_water
