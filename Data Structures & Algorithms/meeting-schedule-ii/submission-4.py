"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[i.start for i in intervals]
        end=[i.end for i in intervals]
        start.sort()
        end.sort()
        print(start,end)
        m=len(intervals)
        counter=0
        max_count=0
        s=0
        e=0
        while(s<m):
            if start[s]<end[e]:
                counter+=1
                max_count=max(max_count,counter)
                s+=1
            else:
                counter-=1
                e+=1                
        return max_count


        


        
       

