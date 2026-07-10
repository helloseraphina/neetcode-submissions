class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # result of intervals
        res = []

        for i in range(len(intervals)):
            # edge cases
            # if end interval of new interval is less than start value of current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval goes after current interval
            elif newInterval[0] > intervals[i][1]:
                # append interval we are currently at
                # because new int not overlapping
                res.append(intervals[i])
            else:
                # new interval overlap with current interval we are at
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        
        return res
