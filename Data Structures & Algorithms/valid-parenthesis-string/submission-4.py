class Solution:
    def checkValidString(self, s: str) -> bool:
        #TC-O(N^2)
        n=len(s)
        memo=[[None]*n for i in range(n)]

        def backtrack(i,opens):
            if opens<0:
                return False
            if i==n:
                return opens==0
            if memo[i][opens] is not None:
                return memo[i][opens]
            
            if s[i]=="(":
                result=backtrack(i+1,opens+1)
            elif s[i]==")":
                result=backtrack(i+1,opens-1)
            else:
                result=(backtrack(i+1,opens) or backtrack(i+1,opens+1) or backtrack(i+1,opens-1))
            
            memo[i][opens]=result
            return memo[i][opens]
    
        return backtrack(0,0)


        #TC-O(N)
        # star=[]
        # left=[]
        # for i,ch in enumerate(s):
        #     if ch=="(":
        #         left.append([ch,i])
        #     elif ch=="*":
        #         star.append([ch,i])
        #     else:
        #         if left:
        #             left.pop()
        #         elif star:
        #             star.pop()
        #         else:
        #             return False
        
        # while star and left:
        #     if star[-1][1]>left[-1][1]:
        #         left.pop()
        #         star.pop()
        #     else:
        #         return False
        
        # return not left
        # if star:
        #     return True
        # if left:
        #     return False 
        # return True
        
            
        
                

        