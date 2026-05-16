class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            max_res=0
            for i in range(0,len(prices)-1):
                for j in range(i+1,len(prices)):
                    max_res=max(max_res,prices[j]-prices[i])
            return (max_res)