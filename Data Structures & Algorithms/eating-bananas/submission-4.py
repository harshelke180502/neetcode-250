class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        ans=R
        while(L<=R):
            mid=(L+R)//2
            total=0
            for p in piles:
                total+=math.ceil(float(p)/mid)
            if total<=h:
                ans=mid
                R=mid-1
            else:
                L=mid+1
        return ans
