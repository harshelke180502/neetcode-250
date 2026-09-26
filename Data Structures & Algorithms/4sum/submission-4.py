class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        a=0
        ans=[]
        while (a<n-3):
            # if nums[a]>target:
            #     return ans
            if a>0 and nums[a]==nums[a-1]:
                a+=1
                continue
            b=a+1
            while (b<n-2):
                if b>a+1 and nums[b]==nums[b-1]:
                    b+=1
                    continue
                c=b+1
                d=n-1
                while (c<d):
                    curr_sum=nums[a]+nums[b]+nums[c]+nums[d]
                    # if c>b+1 and nums[c]==nums[c-1]:
                    #     c+=1
                    # elif d<n-1 and nums[d]==nums[d+1]:
                    #     d-=1
                    if curr_sum==target:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
                        d-=1

                        while c < d and nums[c] == nums[c - 1]:
                            c += 1

                        
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    
                    elif curr_sum<target:
                        c+=1
                    elif curr_sum>target:
                        d-=1
                b+=1
            a+=1

        return ans


                    
                                        



        