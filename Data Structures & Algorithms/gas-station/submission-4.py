class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #TC : O(n)
        if sum(gas)<sum(cost):
            return -1
        total=0
        res=0
        n=len(gas)
        for i in range(n):
            total+=gas[i]-cost[i]
            if total<0:
                total=0
                res=i+1
        return res



        # TC:O(n^2)
        # n=len(gas)
        # total_gas=0
        # total_cost=0
        # if sum(gas)<sum(cost):
        #     return -1
        # for i in range(0,n):
        #     tank=gas[i]-cost[i]
        #     if tank<0:
        #         continue
          
        #     idx=(i+1)%n
        #     while idx!=i:
        #         tank+=(gas[idx]-cost[idx])
        #         if tank<0:
        #             break   
        #         idx=idx+1
        #         idx=idx%n
        #     if idx==i:
        #         return idx
        # return -1
            



        