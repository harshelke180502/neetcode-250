class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subset1=[]
        if sum(nums)%2!=0:
            return False
        n=len(nums)
        target=sum(nums)//2
        dp=[[-1]*(target+1) for _ in range(n+1)]
        def recurse(i,tar):
            if tar==0:
                return True
            if i>=n or tar<0:
                return False  
            if dp[i][tar]!=-1:
                return dp[i][tar]
            
            pick=recurse(i+1,tar-nums[i])
            skip=recurse(i+1,tar)

            dp[i][tar]=pick or skip

            return dp[i][tar]


        
        
        return recurse(0,target)
        



        