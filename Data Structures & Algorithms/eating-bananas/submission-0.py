class Solution:
    from math import ceil
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = 0

        for num in piles:
            maxRate = max(maxRate,num)
        
        left = 1
        right = maxRate
        while left < right:
            k = (left+right) // 2
            totalHours = 0
            for num in piles:
                totalHours += math.ceil(num/k)
            if totalHours > h:
                left = k+1
            else:
                right = k
        
        return right 


        