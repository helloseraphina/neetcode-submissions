class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals.sort(key = lambda x: x[0])
        # init output list with first interval to avoid edge case
        output = [intervals[0]]

        # skip first interval because it is already in output list
        for start, end in intervals[1:]:
            # get most recently added interval in output
            # get end value
            lastEnd = output[-1][1]

            # overlapping
            # if current start is <= lastEnd interval
            if start <= lastEnd:
                # merge last end interval up to max end val
                output[-1][1] = max(lastEnd, end)
            else:
                # non-overlapping
                # append new interval to output list
                output.append([start, end])
        return output
