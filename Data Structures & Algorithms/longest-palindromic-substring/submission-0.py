class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        left_idx=0
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i+1<=3 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if length<j-i+1:
                        length=j-i+1
                        left_idx=i
        return s[left_idx:left_idx+length]

        

        