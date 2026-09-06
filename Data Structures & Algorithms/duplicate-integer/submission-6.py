class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}  # This is our hashmap/dict

        for num in nums:
            if num in count:
                # Already seen once, so now count would be > 1
                return True
            else:
                count[num] = 1  # First time seeing this number
        
        return False
