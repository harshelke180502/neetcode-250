class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map_of_nos=set(nums)
        longest=0
        for num in map_of_nos:
            if num-1 not in map_of_nos:
                length=1
                while(num+length) in map_of_nos:
                    length+=1
                longest=max(length,longest)
        return longest
        