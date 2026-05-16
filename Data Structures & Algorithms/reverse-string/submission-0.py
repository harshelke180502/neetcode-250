class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        i=0
        j=n-1
        if n==1 or n==0:
            return s

        else:

            while(i<j):
                s[i],s[j]=s[j],s[i]
                i=i+1
                j=j-1
            return s
