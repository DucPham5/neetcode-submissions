class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])        
            elif s[i] == '}':
                if stack:
                    last = stack.pop()
                else:
                    last = ""
                if last != '{':
                    return False
            elif s[i] == ')':
                if stack:
                    last = stack.pop()
                else:
                    last = ""
                if last != '(':
                    return False
            elif s[i] == ']':
                if stack:
                    last = stack.pop()
                else:
                    last = ""
                if last != '[':
                    return False
        if stack:
            return False

        return True