class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack=[]
        res=[]
        def backtrack(Open,Closed):
            if Open==Closed==0:
                res.append("".join(stack[:]))
            if Open>0:
                stack.append("(")
                backtrack(Open-1,Closed)
                stack.pop()
            if Open<Closed:
                stack.append(")")
                backtrack(Open,Closed-1)
                stack.pop()
            



        backtrack(n,n)
        return res