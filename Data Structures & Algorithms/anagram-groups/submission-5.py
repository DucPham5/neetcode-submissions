class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in a_map:
                a_map[sorted_string].append(s)
            else:
                a_map[sorted_string] = []
                a_map[sorted_string].append(s)

        
        return list(a_map.values())
        