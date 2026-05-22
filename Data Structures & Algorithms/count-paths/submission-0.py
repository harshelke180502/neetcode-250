class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(i,j,dp):

            if i<0 or j<0:
                return 0

            if i==0 and j==0:
                return 1
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dp[i][j]=dfs(i-1,j,dp)+dfs(i,j-1,dp)
            return dp[i][j]
      
        dp=[[-1]*n for _ in range(m)]
        # print(dp)
        row=m-1
        col=n-1
        return dfs(row,col,dp)
        