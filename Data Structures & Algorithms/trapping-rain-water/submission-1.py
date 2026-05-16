class Solution:
    def trap(self, height: List[int]) -> int:
  

        if len(height)==0:
            return 0
        total=0
        for i in range(0,len(height)):
            left_max=right_max=height[i]

            for left in range(0,i):
                left_max=max(left_max,height[left])
            
            for right in range(i+1,len(height)):
                right_max=max(right_max,height[right])
            
            total=total+(min(left_max,right_max)-height[i])

        return total        