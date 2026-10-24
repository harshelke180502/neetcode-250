class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # i=0
        # prev=0
        # while i<len(nums):
        #     if i>0 and i==prev and i<len(nums)-1:  
        #         return False
        #     if i==len(nums)-1:  
        #         return True    
        #     prev=i
        #     i=i+nums[i]
        # return True
        goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return goal==0

            
        