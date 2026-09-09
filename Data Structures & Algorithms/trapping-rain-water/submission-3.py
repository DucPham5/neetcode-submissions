class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trappedWater = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if stack:
                    currentheight = min(height[stack[-1]],height[i]) - height[top]
                    width = i - stack[-1] - 1
                else:
                    break
                trappedWater += currentheight*width

            stack.append(i)

        return trappedWater

        