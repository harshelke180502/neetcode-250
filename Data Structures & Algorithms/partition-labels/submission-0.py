class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=defaultdict(list)
        for i in range(0,len(s)):
            count[s[i]].append(i)
        intervals=list(count.values())
        # print(intervals)
        start_interval=intervals[0][0]
        end_interval=intervals[0][-1]
        output=[]
        for i in range(1,len(intervals)):
            if start_interval<intervals[i][0]<end_interval:
                end_interval=intervals[i][-1] if intervals[i][-1]>end_interval else end_interval

            else:
                output.append((end_interval-start_interval)+1)
                start_interval=intervals[i][0]
                end_interval=intervals[i][-1]
        output.append((end_interval-start_interval)+1) 
        return output
        