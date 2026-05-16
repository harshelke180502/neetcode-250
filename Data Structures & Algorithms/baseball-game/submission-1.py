class Solution:
    def calPoints(self, operations: List[str]) -> int:
      
        l=[]
        for i in range(len(operations)):
            if operations[i]=="C":
                if l:
                    l.pop()
            elif operations[i]=="+":
                if len(l)>=2:
                    l.append(l[-1]+l[-2])
            elif operations[i]=="D":
                if l:
                    l.append(2*l[-1])
            else:
                l.append(int(operations[i]))
        return sum(l)

                


