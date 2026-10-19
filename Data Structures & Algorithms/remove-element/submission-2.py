class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k=0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k

        i=0
        n=len(nums)
        while i<n:
            if nums[i]==val:
                n-=1
                nums[i]=nums[n]
            else:
                i+=1
        return n


        # i=0
        # j=0
        # k=0
        # while j<len(nums):
        #     if nums[i]==val:
        #         while j<len(nums) and nums[j]==nums[i]:
        #             j+=1
        #         if j<len(nums):
        #             nums[i],nums[j]=nums[j],nums[i]
        #     i+=1
        #     j+=1
        #     if j<len(nums):
        #         k+=1
            
        # print(i)
        # print(nums)
        # return k

                
