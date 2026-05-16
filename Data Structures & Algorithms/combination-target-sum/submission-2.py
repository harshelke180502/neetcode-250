class Solution:
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

            res=[]

            def recurse(ind,cur,total):

                if total==target and cur[:] not in res:
                    res.append(cur[:])
                    return 
                if ind>=len(nums) or total>target:
                    return

                cur.append(nums[ind])
                recurse(ind,cur,total+nums[ind])

                cur.pop()
                recurse(ind+1,cur,total)


                


            

            recurse(0,[],0)
            return res