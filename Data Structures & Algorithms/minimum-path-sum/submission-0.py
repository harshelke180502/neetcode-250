class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(r,c,dp):
            if r<0 or c<0:
                return float("inf")
            if r==0 and c==0:
                return grid[r][c]
            if dp[r][c]!=-1:
                return dp[r][c]
            dp[r][c]=min(grid[r][c]+dfs(r,c-1,dp),grid[r][c]+dfs(r-1,c,dp))
            return dp[r][c]

        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        return dfs(m-1,n-1,dp)
        