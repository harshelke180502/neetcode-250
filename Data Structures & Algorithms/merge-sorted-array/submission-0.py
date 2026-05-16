class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(m,len(nums1)):
            nums1[i]=nums2[i-m]
       

        for k in range(0,m+n):
            l=k

            while(nums1[l-1]>nums1[l] and l>0):
                nums1[l-1],nums1[l]=nums1[l],nums1[l-1]
                l=l-1
        return nums1