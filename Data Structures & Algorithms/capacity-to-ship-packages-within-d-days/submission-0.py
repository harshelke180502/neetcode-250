class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=max(weights)
        r=sum(weights)
        ans=r

        def Ship_possible(mid):
            ships_count=1
            curr_mid=mid
            for w in weights:
                if curr_mid-w<0:
                    ships_count=ships_count+1
                    if ships_count>days:
                        return False
                    curr_mid=mid
                curr_mid=curr_mid-w
            return True
        
        while l<=r:
            mid=(l+r)//2
            if Ship_possible(mid):
                ans=min(ans,mid)
                r=mid-1
            else:
                l=mid+1
        return ans

            


                
        