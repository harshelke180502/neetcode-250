class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums)==1:
            return False
        i=0
        j=1

        while i<len(nums)-1:
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                j+=1
            i+=1
        return False



        