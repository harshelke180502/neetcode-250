class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        suf=[1]*n
        pref=[1]*n
        ans=[1]*n

        for i in range(n-1,-1,-1):
            if i<n-1:
                pref[i]=pref[i]*nums[i+1] *pref[i+1]
        # print(suffix)
        for j in range(0,n):
            if j>0:
                suf[j]=suf[j]*nums[j-1]*suf[j-1]
        # print(prefix)
        for k in range(0,n):
            ans[k]=suf[k]*pref[k]

        # print(ans)
        return ans

        

        



        