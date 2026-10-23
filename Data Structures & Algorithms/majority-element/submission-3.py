class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res=0
        # count=0
        # for num in nums:
        #     if count==0:
        #         res=num
            
        #     if res==num:
        #         count+=1
        #     else:
        #         count-=1
        # return res

        # maxcount=0
        # res=0
        # count={}
        # for n in nums:
        #     count[n]=1+count.get(n,0)
        #     if maxcount<count[n]:
        #         res=n
        #         maxcount=count[n]
        # return res   
        
        count={}
        maxcount=float("-inf")
        res=float("-inf")
        for n in nums:
            count[n]=count.get(n,0)+1
            if maxcount<count[n]:
                maxcount=count[n]
                res=n
        return res





        