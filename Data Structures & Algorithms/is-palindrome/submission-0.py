class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return false

        # 
        s = "".join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(s) - 1 
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True