class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax,globalMin=nums[0],nums[0]
        currMax,currMin=0,0
        total=0

        for n in nums:
            currMax=max(currMax+n,n)
            globalMax=max(globalMax,currMax)
            currMin=min(currMin+n,n)
            globalMin=min(globalMin,currMin)
            total+=n
        if globalMax<0:
            return globalMax
        return max(total-globalMin,globalMax)

