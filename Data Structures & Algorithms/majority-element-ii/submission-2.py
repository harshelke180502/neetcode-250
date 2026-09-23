class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)

        for num in nums:
            count[num]+=1
            if len(count)<=2:
                continue
            new_count=defaultdict(int)
            for n,c in count.items():
                if c > 1:
                    new_count[n]=c-1
            count=new_count
        ans=[]
        for n in count:
            if nums.count(n)>len(nums)//3:
                ans.append(n)
        return ans

        # n=len(nums)
        # d=defaultdict(int)
        # ans=set()
        # for num in nums:
        #     d[num]+=1
        #     if d[num]>n//3 and num not in ans:
        #         ans.add(num)
        #     # print(list(ans))
        # return list(ans)        
