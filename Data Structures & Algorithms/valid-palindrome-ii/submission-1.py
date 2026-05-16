class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1]==s:
            return True
        
        for i in range(0,len(s)):
            new_s=s[:i]+s[i+1:]
            if new_s==new_s[::-1]:
                return True
        return False