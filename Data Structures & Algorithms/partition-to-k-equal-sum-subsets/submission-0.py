class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        target=sum(nums)//k
        used=[False]*len(nums)

        def backtrack(i,k,subarraySum):
            if k==0:
                return True
            if subarraySum==target:
                return backtrack(0,k-1,0)
            prev=-1
            for j in range(i,len(nums)):
                if used[j] or subarraySum+nums[j]>target:
                    continue
                if prev==nums[j]:
                    continue
                
                used[j]=True
                prev=nums[j]
                if backtrack(j+1,k,subarraySum+nums[j]):
                    return True
                used[j]=False

                if subarraySum==0:
                    return False
            return False
        
        return backtrack(0,k,0)
            
            

        
        
        