from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []


        def backtracking(openP, close):

            if openP == close == n:
                res.append("".join(stack))
            
                return
            
            if openP < n:
                stack.append("(")
                backtracking(openP + 1, close)
                stack.pop()
            
            if close < openP:
                stack.append(")")
                backtracking(openP, close + 1)
                stack.pop()
        
        backtracking(0, 0)

        return res