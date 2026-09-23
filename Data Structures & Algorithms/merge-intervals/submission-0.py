class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort(key=lambda x: x[0])
        ans=[intervals[0]]
        for start,end in intervals:
            last=ans[-1][1]
            if last>=start:
                ans[-1][1]=max(last,end)
            else:
                ans.append([start,end])
        return ans
        


        