"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    
        # sort list by start times
        intervals.sort(key=lambda x: x.start)

        # check for overlapping intervals
        for i in range(len(intervals) - 1):
            current_end_time = intervals[i].end
            next_start_time = intervals[i+1].start
            
            # overlaps
            if next_start_time < current_end_time:
                return False
        
        return True