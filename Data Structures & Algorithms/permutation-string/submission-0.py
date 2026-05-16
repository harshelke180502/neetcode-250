class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        l=[]

        for i in range(0,len(s1)):
            l.append(s1[i])
        l1=l.copy()
            # print(l1)
            # print(l)

        for j in range(0,len(s2)-len(s1)+1):
            
            k=j
            while(k<j+n):
                if s2[k] in l:
                    # print(l)
                    # print(s2[k])
                    l.remove(s2[k])
                k=k+1
                
            if l==[]:
             return True

            
            else:
                l=l1.copy()
        return False