class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        def dfs(r,c,dp):
            if r<0 or c<0 or obstacleGrid[r][c]==1:
                return 0
            if r==0 and c==0:
                return 1
            if dp[r][c]!=-1:
                return dp[r][c]
            dp[r][c]=dfs(r-1,c,dp)+dfs(r,c-1,dp)
            return dp[r][c]
        




        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        return dfs(m-1,n-1,dp)