class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_of_nos={}
        cur_sum=0
        counter=0
        map_of_nos[0]=1
        for i in range(0,len(nums)):
            cur_sum+=nums[i]
            if cur_sum-k in map_of_nos:
                counter+=map_of_nos[cur_sum-k]
            
            map_of_nos[cur_sum]=map_of_nos.get(cur_sum,0)+1
          

        return counter

