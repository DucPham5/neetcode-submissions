class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for char in s:
            smap[char] = 1 + smap.get(char, 0)
        
        for char in t:
            tmap[char] = 1 + tmap.get(char,0)
        


        return tmap == smap
        
        