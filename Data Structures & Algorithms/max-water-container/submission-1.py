class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        left = 0
        right = len(heights)-1

        while left < right:
            length = right-left
            height = min(heights[left],heights[right])
            area = length * height
            #print(area)
            maxAmount = max(maxAmount,area)
            if heights[left] < heights[right]:#if lefts height is less we increment cause we dont care about it anymore
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
                right-=1

        return maxAmount

            

        