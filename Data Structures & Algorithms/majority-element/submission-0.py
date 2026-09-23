class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxcount=0
        res=0
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)
            if maxcount<count[n]:
                res=n
                maxcount=count[n]
        return res            

        