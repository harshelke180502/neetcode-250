class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest):
            subarray=1
            curr_sum=0
            for num in nums:
                curr_sum+=num
                if curr_sum>largest:
                    subarray+=1
                    if subarray>k:
                        return False
                    curr_sum=num
            return True
        
        
        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            m=l+(r-l)//2
            if can_split(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
        
        