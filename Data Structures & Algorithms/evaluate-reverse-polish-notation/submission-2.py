class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        ans=0
        for i in range(0,len(tokens)):
            if tokens[i]!="*" and tokens[i]!="+" and tokens[i]!="-" and tokens[i]!="/":
                stack.append(int(tokens[i]))
            else:
                
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == "+":
                    stack.append(b + a)
                elif tokens[i] == "-":
                    stack.append(b - a)
                elif tokens[i] == "*":
                    stack.append(b * a)
                elif tokens[i] == "/":
                   
                    stack.append(int(b / a))
            
            
        return (stack[-1])
        
