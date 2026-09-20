class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}

        for char in s1:
            seen[char] = 1 + seen.get(char, 0)
        
        left = 0
        right = 0
        
        window = {}
        while right < len(s2):
            if window == seen:
                return True
            if (right-left) < len(s1):
                window[s2[right]] = 1 + window.get(s2[right],0)
                right+=1
            else:
                if window[s2[left]] > 1:
                    window[s2[left]] = window.get(s2[left],0) - 1
                else:
                    window.pop(s2[left],None)
                left+=1

            

        return window == seen