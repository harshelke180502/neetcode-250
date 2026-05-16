class Solution:
    def simplifyPath(self, path: str) -> str:

        l=path.split("/")
        
        stack=[]
        for i in l:
            if i=='':
                continue

            elif i==".":
                continue

            elif i=='..':
                if stack:
                    stack.pop()
                else:
                    continue
            
            else:
                stack.append(i)
        


        res=""
        if not stack:
            res=res+"/"
        else:

            for i in stack:
                res=res+"/"+i
        return (res)

                