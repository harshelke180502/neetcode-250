class Solution:
    def isValid(self, s: str) -> bool:

        ans=[]
        flag=False
        for i in range(0,len(s)):
        
        
            if s[i]=="[" or s[i]=="(" or s[i]=="{":
                ans.append(s[i])
                
            elif s[i]==")" :
                if ans and ans[-1]=="(":
                    ans.pop()
                    flag=True

                else:
                    flag=False
                    break
            elif s[i]=="]":
                if ans and ans[-1]=="[" :
                    ans.pop()
                    flag=True
                else:
                    flag=False
                    break
            elif s[i]=="}":
                if ans and ans[-1]=="{": 
                    ans.pop()
                    flag=True
                else:
                    flag=False
                    break

        if ans:
            flag=False

        return flag
        


            














