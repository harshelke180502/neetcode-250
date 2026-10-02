class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        letters={}
        for i in range(len(t)):
            letters[t[i]]=letters.get(t[i],0)+1

        print(letters)

        count=0
        left=0
        resLen=float("inf")
        res=[-1,-1]
        for right in range(len(s)):
            if s[right] in letters:
                # we have enough characters
                if letters[s[right]]>0:
                    count+=1
                letters[s[right]]-=1
            while count==len(t):
                if right-left+1<resLen:
                    resLen=right-left+1
                    res=[left,right]
                if s[left] in letters:
                    # we either have enough or we need more than we have - in that case we reduce the count and we increase the count of have as we shrink
                    if letters[s[left]]>=0:
                        count-=1
                    letters[s[left]]+=1
                left+=1
        left,right=res
        return s[left:right+1]
                




        
        # left,right=0,0
        # count=0
        # res=float("inf")
        # substring=""
        # while(right<len(s)):

        #     if s[right] in letters and letters[s[right]]>0:
        #         letters[s[right]]-=1
        #         count+=1
        #     elif s[right] in letters and letters[s[right]]<=0:
        #         letters[s[right]]+=1
        #         count+=1
                
        #     while letters[right]==0 and count==len(t):
        #         if right-left+1 <= res:
        #             res=right-left+1
        #             substring=s[left:right+1]
        #         if s[left] in letters:
        #             letters[s[left]]-=1
        #             count-=1
        #         left=left+1
            
        #     right=right+1

        # return substring