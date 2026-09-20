class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_water=float("-inf")
        j=n-1
        i=0
        while(i<j):
            max_water=max(max_water,min(heights[i],heights[j])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water
        


            

            

            
            



        