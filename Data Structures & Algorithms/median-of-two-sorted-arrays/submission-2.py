class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2, nums1
        
        A = len(nums1)
        B = len(nums2)

        leftcount = (A+B+1)//2
        low = 0
        high = A

        while low <= high:
            i = (low + high) // 2
            j = leftcount - i

            maxleft1 = nums1[i-1] if i > 0 else float('-inf')
            minright1 = nums1[i] if i < A else float('inf')
            
            maxleft2 = nums2[j-1] if j > 0 else float('-inf')
            minright2 = nums2[j] if j < B else float('inf')

            if maxleft1 > minright2:
                high = i-1
            elif maxleft2 > minright1:
                low = i+1
            else:
                break
        
        if (A+B)%2 == 0:
            median = (max(maxleft1,maxleft2) + min(minright1,minright2)) / 2
        else:
            median = max(maxleft1,maxleft2)
        
        return median

            
             
        
        