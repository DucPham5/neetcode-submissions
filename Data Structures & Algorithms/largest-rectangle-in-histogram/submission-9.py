class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largestArea = 0

        for i in range(len(heights)):
            currentArea = 0
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i - 0
                currentArea = width * heights[top]
                largestArea = max(currentArea, largestArea)
            
            stack.append(i)
        
        while stack:
            top = stack.pop()
            if stack:
                width = len(heights) - stack[-1] -1
            else:
                width = len(heights) - 0
            

            currentArea = heights[top] * width
            largestArea = max(currentArea, largestArea)
            
        
        return largestArea