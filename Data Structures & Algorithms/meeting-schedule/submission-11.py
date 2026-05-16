"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:

            return True

        
        intervals.sort(key= lambda i: i.start)

        output=[intervals[0]]

        

        for i in intervals[1:]:

            lastend=output[-1].end

            if i.start<lastend:

                return False

            else:

                output.append(i)

        return True


        
