class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=collections.deque()
        l=0
        r=0
        output=[]
        while r<len(nums):

            #popping the smaller elements inside the current frame
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            
            #shrinking the window and keeping the window updated
            if l>q[0]:
                q.popleft()
            
            #checking if r is the last idx of the window of k
            if r+1>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output


        
                
