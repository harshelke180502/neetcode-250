class Solution:
    def f(self,n,dp):
        if n<=2:
            return n
        if dp[n]!=0:
            return dp[n]
        dp[n]=self.f(n-1,dp)+self.f(n-2,dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        return self.f(n,dp)

        
        