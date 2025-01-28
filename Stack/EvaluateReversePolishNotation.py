from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                three, four = stack.pop(), stack.pop()
                stack.append(four - three)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                one, two = stack.pop(), stack.pop()
                stack.append(int(float(two) / float(one)))
            else:
                stack.append(int(i))
        return stack[0]
                
                
