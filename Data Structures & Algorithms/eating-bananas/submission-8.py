class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=max(piles)
        
        while(l<=r):
            k=l+((r-l)//2)
            total=0
            for i in range(len(piles)):
                total+=math.ceil(float(piles[i])/k)
            if total<=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res




