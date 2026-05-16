class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                d={}

                i=0
                # d[nums[i]]=0
                while(i<len(nums)):
                    if nums[i] not in d.keys():
                        d[nums[i]]=1 

                    else:
                    
                        d[nums[i]]=d[nums[i]]+1
                    i=i+1
                result=[]    

                for key,val in d.items():
                # if d[key]>=k:
                #   result.append(key)
                    result.append(d[key])
                

                for s in range(len(result)-1,-1,-1):
                    for t in range(0,s):
                        if result[t]<result[t+1]:
                            result[t],result[t+1]=result[t+1],result[t]
                

                final=set()
                for value in range(0,k):
                    for k,v in d.items():
                        if (result[value]==v and k not in final):
                            final.add(k)
                return list(final)




    
          
