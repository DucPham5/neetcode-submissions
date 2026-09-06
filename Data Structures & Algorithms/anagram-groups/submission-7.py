class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for x in s:
                index = ord(x) - ord("a")
                count[index] += 1
            
            output[tuple(count)].append(s)
        
        result = []
        for value in output.values():
            result.append(value)

            
        
        return result
