class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = {}
        for st in strs:
            sorted_string = ''.join(sorted(st))
            if sorted_string in aMap:
                aMap[sorted_string].append(st)
            else:#if the key is just being added initialize an empty array then append
                aMap[sorted_string] = []
                aMap[sorted_string].append(st)
            
        return aMap.values()

