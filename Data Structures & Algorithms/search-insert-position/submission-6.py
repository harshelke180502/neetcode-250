class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # #using lower bound
        # l,r=0,len(nums)
        # while l<r:
        #     m=l+(r-l)//2
        #     if target<=nums[m]:
        #         r=m
        #     else:
        #         l=m+1
        # return l
        l,r=0,len(nums)-1
        while l<=r:
            m=l+((r-l)//2)
            if target==nums[m]:
                return m
            elif target>nums[m]:
                l=m+1
            else:
                r=m-1
        return l
            


