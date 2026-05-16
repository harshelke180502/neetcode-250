class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()

        if len(s)==1:
            return True

        if len(s)==0:
            return False

        l=[]
        for i in s:
            if i.isalnum():
                l.append(i)

        l1=l.copy()
        # print(l1)
        n=len(l)
        a=0
        b=n-1
        # ans=False
        while(a<b):
        
            l1[a],l1[b]=l1[b],l1[a]
            a=a+1
            b=b-1
            
        
        if l1 == l:
            return True
        else:
            return False