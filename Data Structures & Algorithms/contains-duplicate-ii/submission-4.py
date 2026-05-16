class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        flag=False
        # while(i<len(nums)-k):

        #     j=i+1

        #     while(j<=min(len(nums),i+k)):
        #         if nums[i]==nums[j]:
        #             flag=True
        #             break
        #         j=j+1
        #     i=i+1
        # return flag
        for i in range(0,len(nums)):
            for j in range(i+1,min(len(nums),i+k+1)):
                 if nums[i]==nums[j]:
                    return True
        return False