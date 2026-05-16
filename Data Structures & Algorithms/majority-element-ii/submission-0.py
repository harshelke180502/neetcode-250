class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=list(set(nums))
        len_l=len(l)
        i=0
        j=0
        d={}
        count=0
        while(i<len_l and j<n):
            if l[i] == nums[j]:
                count=count+1
            j=j+1

            if(j==n):
                d[l[i]]=count
                j=0
                count=0
                i=i+1
        # print(d)
        final_ans=[]
        for i in d:
        # print(i)
            if d[i]>n//3:
                final_ans.append(i)
        return final_ans




            