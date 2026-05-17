class Solution:
    def backtrack(self,idx,dp,nums):
        if idx<0:
            return 0 
        if dp[idx]!=0:
            return dp[idx]
        rob=nums[idx]+self.backtrack(idx-2,dp,nums)
        skip=self.backtrack(idx-1,dp,nums)
        dp[idx]=max(rob,skip)
        return dp[idx]
        

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        return self.backtrack(n-1,dp,nums)

        