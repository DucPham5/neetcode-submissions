class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointer approach 
        left = 0
        right = len(height)-1
        leftmax = height[left]
        rightmax = height[right]
        result = 0

        while left < right:
            if leftmax < rightmax:
                result += leftmax - height[left]
                left+=1
                leftmax = max(leftmax, height[left])
            else:
                result += rightmax - height[right]
                right-=1
                rightmax = max(rightmax, height[right])     

        return result         
