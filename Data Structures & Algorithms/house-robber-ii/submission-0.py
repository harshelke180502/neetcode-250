class Solution:
    def f(self,i,dp,nums):
        if i>=len(nums):
            return 0
        if dp[i]!=-1:
            return dp[i]
        rob=nums[i]+self.f(i+2,dp,nums)
        skip=self.f(i+1,dp,nums)
        dp[i]=max(rob,skip)
        return dp[i]


    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp1=[-1]*n
        dp2=[-1]*n
        ans1=self.f(0,dp1,list(nums[0:n-1]))
        ans2=self.f(0,dp2,list(nums[1:n]))
        return max(ans1,ans2)




        