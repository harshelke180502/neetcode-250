class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        
        def recurse(ind,cur):
            if len(cur)==k:
                res.append(cur[:])
                return
            
            if ind>n:
                return

            # for i in range(ind,n+1):
            #     cur.append(i)
            #     recurse(i+1,cur)
            #     cur.pop()
            cur.append(ind)
            recurse(ind+1,cur)
            cur.pop()
            recurse(ind+1,cur)            

        
        recurse(1,[])
        return res
