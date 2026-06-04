class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i,target):
            if i==len(nums):
                return 1 if target==0 else 0
            if (i,target) in memo:
                return memo[(i,target)]
            memo[(i,target)]=dfs(i+1,target+nums[i])+dfs(i+1,target-nums[i])
            return memo[(i,target)]
        
        return dfs(0,target)
        