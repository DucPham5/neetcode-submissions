class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        output = 0

        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i-1])
        
        for i in range(len(height)-2,-1,-1):
            rightmax[i] = max(rightmax[i+1], height[i+1])

        for i in range(len(height)):
            current = min(leftmax[i], rightmax[i]) - height[i]
            if current > 0:
                output += current
            
        return output
        