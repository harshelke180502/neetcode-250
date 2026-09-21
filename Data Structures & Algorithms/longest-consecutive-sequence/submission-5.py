class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map_of_nos=set(nums)
        longest=0
        max_counter=float("-inf")
        for i in range(len(nums)):
            if nums[i]-1 not in map_of_nos:
                length=1
                while(nums[i]+length) in map_of_nos:
                    length+=1
                longest=max(length,longest)
        return longest
        