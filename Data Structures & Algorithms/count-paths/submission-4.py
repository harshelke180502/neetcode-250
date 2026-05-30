class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
       def dfs(row,col,dp):
            if row<0 or col<0:
                return 0
            if row==0 and col==0:
                return 1
            if dp[row][col]!=-1:
                return dp[row][col]
            dp[row][col]=dfs(row-1,col,dp)+dfs(row,col-1,dp)
            return dp[row][col]     

       dp=[[-1]*n for _ in range(m)]
       return dfs(m-1,n-1,dp)