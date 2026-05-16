class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        window,countT={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        have,need=0,len(countT)

        l=0
        res,minRes=[-1,-1],float("infinity")
        for r in range(0,len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have=have+1
            
            while(have==need):
                if(r-l+1)<minRes:
                    res=[l,r]
                    minRes=r-l+1
                window[s[l]]=window[s[l]]-1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l=l+1
        l,r =res

        if len(res)!=float("infinity"):
            return s[l:r+1]
        else:
            return ""

                

