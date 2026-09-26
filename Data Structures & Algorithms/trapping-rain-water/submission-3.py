class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n
        leftmax[0]=height[0]
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i])
        
        rightmax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])

        res=0
        for i in range(n):
            res+=min(rightmax[i],leftmax[i])-height[i]
        return res
        
        # l,r=0,len(height)-1
        # leftmax,rightmax=height[l],height[r]
        # res=0
        # while (l<r):
        #     if leftmax<rightmax:
        #         l+=1
        #         leftmax=max(leftmax,height[l])
        #         res+=leftmax-height[l]
        #     else:
        #         r-=1
        #         rightmax=max(rightmax,height[r])
        #         res+=rightmax-height[r]
        # return res





                




                
            


        