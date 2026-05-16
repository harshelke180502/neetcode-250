class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in range(0,len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                res=""
                while stack[-1]!="[":
                    res=stack.pop()+res
                stack.pop()
                
                no=""
                while stack and stack[-1].isdigit():
                    no=stack.pop()+no
                stack.append(int(no)*res)
        return "".join(stack)


