class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            n=len(nums)
            for i in range(0,n):
                j=i
                while(j>0 and nums[j-1]>nums[j]):
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                    j=j-1
           

            a=0
            b=a+1
            c=n-1
            ans=[]

            for a in range(0,n-2):
                if a>0 and nums[a]==nums[a-1]:
                    continue
                b=a+1
                c=n-1
                while(b<c):
                    if nums[a]+nums[b]+nums[c]==0 and [nums[a],nums[b],nums[c]] not in ans:
                        ans.append([nums[a],nums[b],nums[c]])
                        b=b+1
                        c=c-1
                        while(b<c and nums[b]==nums[b-1]):
                            b=b+1
                        
                        while(b<c and nums[c]==nums[c+1]):
                            c=c-1
                    
                    if nums[a]+nums[b]+nums[c]<0:
                        b=b+1
                    
                    if nums[a]+nums[b]+nums[c]>0:
                        c=c-1

            return ans
