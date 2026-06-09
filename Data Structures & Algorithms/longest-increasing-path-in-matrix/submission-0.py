class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        def dfs(i,j,prev):
            if i<0 or i>=rows or j<0 or j>=cols or matrix[i][j]<=prev:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            res=1
            res=max(res,1+dfs(i-1,j,matrix[i][j]))
            res=max(res,1+dfs(i+1,j,matrix[i][j]))
            res=max(res,1+dfs(i,j-1,matrix[i][j]))
            res=max(res,1+dfs(i,j+1,matrix[i][j]))
            dp[i][j]=res
            return res


        return max(dfs(r,c,-1) for r in range(rows) for c in range(cols))
