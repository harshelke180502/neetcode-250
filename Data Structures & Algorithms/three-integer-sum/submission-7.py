class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        n=len(nums)
        i=0
        left=1
        right=n-1
        ans=[]
        while(i<n-2):
            if nums[i]>0:
                return ans
            if nums[i]==nums[i-1] and i>0:
                i+=1
                continue
            left=i+1
            right=n-1 
            while(left<right):
                curr_sum=nums[i]+nums[left]+nums[right]
                if left>i+1 and nums[left]==nums[left-1]:
                    left+=1
                elif right<n-1 and nums[right]==nums[right+1]:
                    right-=1
                elif curr_sum==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif curr_sum<0:
                    left+=1
                else:
                    right-=1    
            i+=1

        return ans
            








                

            


           



        
        