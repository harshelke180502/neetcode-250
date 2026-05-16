class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
                tot=0
                l=0
                min_pos=float('inf')
                for r in range(len(nums)):
                    tot=tot+nums[r]
                
                    while(tot>=target):
                        pos=r-l+1
                        min_pos=min(min_pos,pos)
                        # print(min_pos)
                        tot=tot-nums[l]
                        l=l+1

                    

                
                

                    

                
                
                if min_pos==float('inf'):
                    min_pos=0
                return (min_pos)
