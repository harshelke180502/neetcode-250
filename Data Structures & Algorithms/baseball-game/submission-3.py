class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        curr_sum=0
        for i in range(len(operations)):
            if operations[i]=="C":
                curr_sum-=stack[-1]
                stack.pop()
                continue
            elif operations[i]=="D":
                stack.append(stack[-1]*2)
            elif operations[i]=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(operations[i]))
            curr_sum+=stack[-1]
        # print(stack)
        # print(sum(stack))
        return curr_sum