import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+': operator.add, '-': operator.sub,'*': operator.mul,'/': operator.truediv}
        output = 0
        for token in tokens:
            if token in operands:
                value1 = stack.pop()
                value2 = stack.pop()
                output = operands[token](int(value2),int(value1))
                stack.append(output)
            else:
                stack.append(token)
            
        return int(stack[-1])
        