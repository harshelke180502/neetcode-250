class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(i,cur,total):
            if i>=n:
                return total
            cur.append(nums[i])
            take=dfs(i+1,cur,total^nums[i])
            cur.pop()
            not_take=dfs(i+1,cur,total)
            return take+not_take


                



        return(dfs(0,[],0))
        