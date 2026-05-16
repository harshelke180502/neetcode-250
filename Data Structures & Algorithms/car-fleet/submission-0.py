class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

                l=[]
                for p,s in zip(position,speed):
                    l.append((p,s))
                
                l.sort(reverse=True)
                
                stack=[]
                
                for i,j in l:
                    stack.append((target-i)/j)
                    if len(stack)>=2 and stack[-1]<=stack[-2]:
                        stack.pop()
                return(len(stack))
        