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

        intervals.sort(key=lambda item:item.start)
        lastend=intervals[0].end
        
        for i in range(1,len(intervals)):
            curr_start=intervals[i].start
            if curr_start<lastend:
                return False
            lastend=intervals[i].end
        return True
        # ans=[intervals[0]]
        # flag=True

        # for i in range(1,len(intervals)):



        #     if intervals[i].start<=ans[-1].end:
        #         flag=False
        #         return flag
        #     else:
        #         ans.append(intervals[i])
        
        # return flag






































        # if not intervals:

        #     return True

        
        # intervals.sort(key= lambda i: i.start)

        # lastend=intervals[0].end

        

        # for i in range(1,len(intervals)):

            

        #     if intervals[i].start<lastend:

        #         return False

        #     lastend = intervals[i].end 

        # return True


        
