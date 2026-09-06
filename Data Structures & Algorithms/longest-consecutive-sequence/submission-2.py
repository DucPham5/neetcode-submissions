class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            s = set()

            for num in nums:
                s.add(num)

            longest = 0
            for x in s:
                if (x-1) not in s:
                    count = 0
                    while x in s:
                        x+=1
                        count+=1
                    longest=max(count,longest)

            return longest
        