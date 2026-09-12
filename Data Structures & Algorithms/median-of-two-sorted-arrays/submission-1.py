class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        n = len(nums1)
        m = len(nums2)
        leftcount = (m+n+1)//2
        total = m+n
    
        low = 0
        high = n
        
            
        while low <= high:
            i = (low+high)//2
            j = leftcount - i

            if i == 0:
                maxleft1 = float('-inf')
            else:
                maxleft1 = nums1[i-1]
            
            if i == n:
                minright1 = float('inf')
            else:
                minright1 = nums1[i]

            if j == 0:
                maxleft2 = float('-inf')
            else:
                maxleft2 = nums2[j-1]
            
            if j == m:
                minright2 = float('inf')
            else:
                minright2 = nums2[j]
            
            if maxleft1 > minright2:
                high = i - 1
            elif maxleft2 > minright1:
                low = i + 1
            else:
                break
        
        if total%2 == 0:
            median = (max(maxleft1, maxleft2) + (min(minright1,minright2))) / 2
        else:
            median = max(maxleft1,maxleft2)
        
        return median

        