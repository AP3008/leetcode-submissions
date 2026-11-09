class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        for t in tokens:
            if t in operators:
                v2 = stack.pop()
                v1 = stack.pop()
                if t == "+":
                    stack.append(v1+v2)
                elif t == "-":
                    stack.append(v1-v2)
                elif t == "*":
                    stack.append(v1*v2)
                else:
                    stack.append(int(v1/v2))
            else:
                stack.append(int(t))
        return stack.pop()