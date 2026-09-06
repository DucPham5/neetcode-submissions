class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s

        return res
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        i = 0
        # 4#leet4#code
        while i < len(s):
            num = 0
            while s[i] != "#":
                num = 10*num + int(s[i])
                i += 1
            i += 1
            temp = ""
            while num > 0:
                temp += s[i]
                i += 1
                num -= 1
            res.append(temp)
        
        return res