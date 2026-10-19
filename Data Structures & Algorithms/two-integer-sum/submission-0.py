class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for idx,num in enumerate(nums):
            diff=target-nums[idx]
            if diff in count.keys():
                return [count[diff],idx]
            count[num]=idx
        
        