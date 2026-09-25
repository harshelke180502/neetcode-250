class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=[]
        right=[]
        for l in word1:
            left.append(l)
        
        for r in word2:
            right.append(r)

        arr=[]
        i,j=0,0
        bools=False

        while(i<len(left) and j<len(right)):
            if bools==False:
                arr.append(left[i])
                i+=1
            else:
                arr.append(right[j])
                j+=1
            bools=not(bools)
        
        while i<len(left):
            arr.append(left[i])
            i+=1

        while j<len(right):
            arr.append(right[j])
            j+=1
        
        return "".join(arr)
        


        