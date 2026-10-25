class Solution:
    def jump(self, nums: List[int]) -> int:
        dp={}
        def dfs(i,dp):
            if i==len(nums)-1:
                return 0
            if nums[i]==0:
                return 1000000
            if i in dp:
                return dp[i]
            res=1000000
            end=min(len(nums),nums[i]+i+1)
            for no in range(i+1,end):
                res=min(res,1+dfs(no,dp))
            dp[i]=res
            return dp[i]
        return dfs(0,dp)





        