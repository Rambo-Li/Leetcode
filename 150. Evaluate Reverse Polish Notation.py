class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                res = str(int(eval(n1+i+n2)))
                stack.append(res)
        return int(stack.pop())