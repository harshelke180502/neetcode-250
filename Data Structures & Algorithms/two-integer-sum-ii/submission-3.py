class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
                n=len(numbers)
                i=0
                j=n-1
                total=0
                l=[]
                while(i<j):

                    total=numbers[i]+numbers[j]

                    if(total==target):
                        l=[i+1,j+1]
                        return l
                    else:
                        j=j-1
                        total=0
                    
                    if i==j:
                        i=i+1
                        j=n-1
