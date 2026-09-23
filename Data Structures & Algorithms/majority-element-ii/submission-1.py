class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d=defaultdict(int)
        ans=set()
        for num in nums:
            d[num]+=1
            if d[num]>n//3 and num not in ans:
                ans.add(num)
            # print(list(ans))
        return list(ans)        
