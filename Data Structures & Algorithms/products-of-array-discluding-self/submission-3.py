class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        ans=[1]*n

        for i in range(n-1,-1,-1):
            if i<n-1:
                suffix[i]=suffix[i]*nums[i+1] *suffix[i+1]
        # print(suffix)
        for j in range(0,n):
            if j>0:
                prefix[j]=prefix[j]*nums[j-1]*prefix[j-1]
        # print(prefix)
        for k in range(0,n):
            ans[k]=prefix[k]*suffix[k]

        # print(ans)
        return ans

        

        



        