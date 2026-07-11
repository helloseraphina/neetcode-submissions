class Solution:
    # time complexity O(nlogn)
    # space complexity O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort all intervals by start time
        intervals.sort(key=lambda x: x[0])
        # init result list output with first interval
        output = [intervals[0]]

        # iterate thru each interval (start, end) in sorted list
        for start, end in intervals:
            # end of the last interval in output
            lastEnd = output[-1][1]
            # if current interval overlaps with last one
            if start <= lastEnd:
                # merge by updating the end of the last interval
                output[-1][1] = max(lastEnd, end)
            # otherwise there is no overlap
            # so append current interval to output as new interval
            else:
                output.append([start, end])
        # after processing all intervals, return output
        return output
    

        