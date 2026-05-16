class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res=""
        n=min(len(word1),len(word2))

        for i in range(0,n):
            res=res+word1[i]+word2[i]

        ans=res   

        if(len(word2)>n):
      
            for k in range(n,len(word2)):
                res=res+word2[k]
                ans=res

        if(len(word1)>n):

            for l in range(n,len(word1)):
                res=res+word1[l]
                ans=res
        return ans