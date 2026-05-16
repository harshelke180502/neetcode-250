class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        i=0
        product=1
        output=[]
        j=0
        while(i<len(nums)):
          if(j!=i):
            product=product*nums[j]
            j=j+1
          else:
            j=j+1
          
          if j==len(nums):
            output.append(product)
            product=1
            j=0
            i=i+1
        return output

        
        
          