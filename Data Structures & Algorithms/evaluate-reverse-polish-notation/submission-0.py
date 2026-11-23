class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a = 0
        b = 0
        for n in tokens:
            if n == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif n == '*':
                a = stack.pop()
                b = stack.pop() 
                stack.append(a*b)
            elif n == '-':
                a = stack.pop()
                b = stack.pop() 
                stack.append(b-a)
            elif n == '/':
                a = stack.pop()
                b = stack.pop() 
                result = abs(b) // abs(a)
                if (b < 0) != (a < 0):
                    result = -result
                stack.append(result)
            else:
                stack.append(int(n))

        return stack.pop()
            





        
        