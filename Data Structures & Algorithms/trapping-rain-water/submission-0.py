class Solution:
    def trap(self, height: List[int]) -> int:
        totalTrapped = 0
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        for i in range(1,len(height)):
            leftmax[i] = max(leftmax[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1],height[i+1])

        for i in range(len(height)):
            currentTrapped = min(leftmax[i],rightmax[i]) - height[i]
            if currentTrapped > 0:
                totalTrapped = totalTrapped + currentTrapped

        return totalTrapped
        