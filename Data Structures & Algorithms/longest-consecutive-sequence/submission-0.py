class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = {}

        for i, num in enumerate(nums):
            seen[num] = 1 + seen.get(num, 0)

        for key in seen.keys():
            counter = 1
            if key-1 not in seen:
                while key+1 in seen:
                    key += 1
                    counter += 1
                if counter > longest:
                    longest = counter

        return longest
            
        