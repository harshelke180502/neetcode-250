class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        total=0
        left=0
        for right in range(len(s)):
            d[s[right]]=1+d.get(s[right],0)

            while((right-left+1)-max(d.values())>k):
                d[s[left]]-=1
                left=left+1
            total=max(total,right-left+1)
        return total
            
        