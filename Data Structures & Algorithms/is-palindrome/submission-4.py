class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        while left < right:
            print(right)
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left+=1 #increment left
            right-=1 #decrement right
        
        return True
        