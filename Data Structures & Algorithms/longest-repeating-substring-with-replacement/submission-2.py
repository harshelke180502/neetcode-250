class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        total=0
        left=0
        max_frequency=0
        for right in range(len(s)):
            d[s[right]]=1+d.get(s[right],0)
            max_frequency=max(max_frequency,d[s[right]])

            while((right-left+1)-max_frequency>k):
                d[s[left]]-=1
                left=left+1
            total=max(total,right-left+1)
        return total
            
        