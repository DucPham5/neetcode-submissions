class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = Counter()

        for char in t:
            seen[char] += 1

        left = 0 
        right = 0

        window = Counter()
        count = 0
        length = float('inf')
        substring = (0,0)
        while right < len(s) or count == len(t):
            #shrinking
            while count == len(t):
                if s[left] in seen and window[s[left]] <= seen[s[left]]:
                    count -= 1
                if (right-left) < length:
                    length = (right-left)
                    substring = (left,right)
                window[s[left]] -= 1
                left+=1
            
            if right < len(s):
                window[s[right]]+=1
                #add to count 
                if s[right] in seen and window[s[right]] <= seen[s[right]]:
                    count += 1
                right+=1 
        
        if length == float('inf'):
            result = ""
        else:
            start, end = substring
            result = s[start:end]
        
        return result
            
            
            
            
            


        