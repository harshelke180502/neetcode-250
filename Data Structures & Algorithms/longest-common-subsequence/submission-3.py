class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo={}
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        # def recurse(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     if text1[i]==text2[j]:
        #         memo[(i,j)]=1+recurse(i+1,j+1)
        #     else:
        #         memo[(i,j)]=max(recurse(i+1,j), recurse(i,j+1))
        #     return memo[(i,j)]
            

        # return recurse(0,0)