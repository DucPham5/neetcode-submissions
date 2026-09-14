class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            count = [0]*26
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1

            seen[tuple(count)].append(s)

        return list(seen.values())
        