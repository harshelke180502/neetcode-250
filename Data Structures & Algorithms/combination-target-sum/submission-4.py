class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def recurse(i,cur,total):
            if total==target:
                ans.append(cur[:])
                return
            
            if i>=len(nums) or total>target:
                return

            #you append whether or not you stay at the same element and stay there or move forward
            cur.append(nums[i])
            #1. Stay at the same element
            recurse(i,cur,total+nums[i])

            #2. to remove the added element that helps us in the third condition: keep the current and move forward
            cur.pop()
            #3. move forward and ignore the current element
            recurse(i+1,cur,total)

        
        recurse(0,[],0)
        return ans