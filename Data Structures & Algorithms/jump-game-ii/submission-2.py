class Solution:
    def jump(self, nums: List[int]) -> int:
        #bfs solution
        l,r=0,0
        #counter to count the number of band jumps
        res=0
        #until it reaches the last level
        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            res+=1
        return res




        # dp={}
        # def dfs(i,dp):
        #     if i==len(nums)-1:
        #         return 0
        #     if nums[i]==0:
        #         return 1000000
        #     if i in dp:
        #         return dp[i]
        #     res=1000000
        #     end=min(len(nums),nums[i]+i+1)
        #     for no in range(i+1,end):
        #         res=min(res,1+dfs(no,dp))
        #     dp[i]=res
        #     return dp[i]
        # return dfs(0,dp)





        