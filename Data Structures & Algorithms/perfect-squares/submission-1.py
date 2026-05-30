class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        for target in range(1,n+1):
            for s in range(1,int(target**0.5)+1):
                square=s*s
                dp[target]=min(1+dp[target-square],dp[target])
        return dp[n]


        