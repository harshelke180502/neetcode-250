class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n

        def recurse(i):
            if dp[i]!=-1:
                return dp[i]
            LIS=1
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    LIS=max(LIS,1+recurse(j))
            dp[i]=LIS
            return dp[i]
        

        max_val=float("-inf")
        for i in range(n):
            max_val=max(max_val,recurse(i))
        return max_val
