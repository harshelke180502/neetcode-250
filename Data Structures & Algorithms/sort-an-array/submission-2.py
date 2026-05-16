import random
class Solution:
    
    def partition(self,nums,low,high):
        
        rand_index = random.randint(low, high)
        nums[low], nums[rand_index] = nums[rand_index], nums[low]
        pivot = nums[low]
        i = low
        j = high
        while(i<j):

            while(nums[i]<=pivot and i<=high-1):
                i=i+1
            while(nums[j]>pivot and j>=low):
                j=j-1
            
            if(i<j):
                nums[i],nums[j]=nums[j],nums[i]
            
        nums[low],nums[j]=nums[j],nums[low]
        return j

    def qs(self,nums,low,high):
        if(low<high):
            p_Index=self.partition(nums,low,high)
            self.qs(nums,low,p_Index-1)
            self.qs(nums,p_Index+1,high)
   
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.qs(nums,0,len(nums)-1)
        return nums

