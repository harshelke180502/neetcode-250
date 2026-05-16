class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        visited=[[False for _ in range(COLS)] for _ in range(ROWS)]
        counter=0
        directions=[[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return 
            if visited[r][c]==True or grid[r][c]=="0":
                return 

            visited[r][c]=True
            for dr,dc in directions:
                dfs(r+dr,c+dc)                
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and not visited[r][c]:
                    dfs(r,c)
                    counter+=1

        return counter
        
        



        