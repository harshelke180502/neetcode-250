class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSub=nums[0]
        # curr_sum=0
        # for num in nums:
        #     if curr_sum<0:
        #         curr_sum=0
        #     curr_sum+=num
        #     maxSub=max(maxSub,curr_sum)
        # return maxSub

        memo=[[None]*2 for _ in range(len(nums))]

        def dfs(i,flag):
            if i==len(nums)-1:
                return max(0,nums[i]) if flag else nums[i]

            if memo[i][flag] is not None:
                return memo[i][flag]
            
            if flag:
                memo[i][flag]=max(0,nums[i]+dfs(i+1,True))
            
            else:
                memo[i][flag]=max(dfs(i+1,False),nums[i]+dfs(i+1,True))
            
            return memo[i][flag]


        return dfs(0,False)