class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(0,n):

            j=i

            while(j>0 and nums[j-1]>nums[j]):
                
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j=j-1
        return nums