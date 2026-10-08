class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #upper bound
        l=0
        r=len(nums)
        while l<r:
            mid=l+((r-l)//2)
            if target<=nums[mid]:
                r=mid
            elif target>nums[mid]:
                l=mid+1
    
        return l if (l<len(nums) and nums[l]==target) else -1
        