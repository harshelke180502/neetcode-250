class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        string=[]
        for char in s:
            if char.isalnum():
                string.append(char)
                
        string1=string.copy()
        l=0
        r=len(string)-1
        while l<r:
           string1[l],string1[r]=string1[r],string1[l]
           l+=1
           r-=1
        if string1==string:
            return True
        else:
            return False
            

        


        