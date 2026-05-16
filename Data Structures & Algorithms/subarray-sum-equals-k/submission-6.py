from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        curr_sum=0
        prefix_dict=defaultdict(int)
        prefix_dict[0]=1

        for n in range(0,len(nums)):
            curr_sum=curr_sum+nums[n]
            diff=curr_sum-k
            count=count+prefix_dict[diff]
            prefix_dict[curr_sum]+=1
            
        return count

