class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
                a=[]
                n=len(arr)
                for i in range(0,n):
                    a.append((arr[i],abs(arr[i]-x)))


                # print(d)
                # print(len(d))
                # a=list(d.items())
                # print(a)



                for i in range(0,len(a)):
                
                    j=i
                    while(j>0 and a[j][1]<a[j-1][1]):
                        a[j],a[j-1]=a[j-1],a[j]
                        j=j-1
                ans=a[:k]
                # print(ans)


                for i in range(0,len(ans)):
                
                    j=i
                    while(j>0 and ans[j][0]<ans[j-1][0]):
                        ans[j],ans[j-1]=ans[j-1],ans[j]
                        j=j-1
                # print(ans)

                result=[]
                for i in ans:
                    result.append(i[0])
                return result