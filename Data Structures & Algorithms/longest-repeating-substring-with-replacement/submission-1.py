class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = [0]*26
        longest = 0
        while right < len(s):
            index = ord(s[right]) - ord('A')
            count[index] += 1
            while (right-left+1) - max(count) > k:
                index = ord(s[left]) - ord('A')
                count[index] -= 1
                left+=1
            
            longest = max(longest,right-left+1)
            right+=1
        
        return longest

        