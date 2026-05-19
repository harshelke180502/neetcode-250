class Solution:
    
    
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp=[amount+1]*(amount+1)
        dp[0]=0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1
        



        # memo={}
        # def dfs(amt):
        #     if amt==0:
        #         return 0
        #     if amt in memo:
        #         return memo[amt]
        #     res=float("inf")
        #     for coin in coins:
        #         if amt-coin>=0:
        #             res=min(res,1+dfs(amt-coin))
        #     memo[amt]=res
        #     return res
                


        # return -1 if dfs(amount)>=float("inf") else dfs(amount)
        