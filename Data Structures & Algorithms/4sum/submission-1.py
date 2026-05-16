class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
                    n=len(nums)
                    ans=[]
                    for i in range(0,n):
                        j=i
                        while(j>0 and nums[j-1]>nums[j]):
                            nums[j-1],nums[j]=nums[j],nums[j-1]
                            j=j-1
                    # print(nums)

                    for a in range(0,n-3):
                        if a>0 and nums[a]==nums[a-1]:
                            continue
                        b=a+1
                    

                        for b in range(a+1,n-2):
                            if b>a+1 and nums[b]==nums[b-1]:
                                continue

                            c=b+1
                            d=n-1
                            while(c<d):
                            
                            
                                if nums[a]+nums[b]+nums[c]+nums[d]==target and [nums[a],nums[b],nums[c],nums[d]] not in ans:
                                    ans.append([nums[a],nums[b],nums[c],nums[d]])
                                    c=c+1
                                    d=d-1
                                    while(c<d and nums[c]==nums[c-1]):
                                        c=c+1
                                    
                                    while(c<d and nums[d]==nums[d+1]):
                                        d=d-1
                            
                                if nums[a]+nums[b]+nums[c]+nums[d]<target:
                                    c=c+1
                                
                                if nums[a]+nums[b]+nums[c]+nums[d]>target:
                                    d=d-1

                    return ans