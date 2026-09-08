class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = 0
        for nums in piles:
            maxRate = max(nums, maxRate)
        
        left = 1
        right = maxRate

        while left < right:
            mid = (left + right) // 2
            totalHours = 0
            for num in piles:
                totalHours += math.ceil(num/mid)
            
            if totalHours > h:
                left = mid + 1
            else:
                right = mid

        
        return left

        
        