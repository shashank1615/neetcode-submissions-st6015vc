class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for s in logs:
            if s == '../':
                if stack:
                    stack.pop()
            elif s == './':
                continue
            else:
                stack.append(s)
        return len(stack)