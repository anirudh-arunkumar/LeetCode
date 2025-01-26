class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
    
        paren_map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        stack = []

        for p in s:

            if p in "({[":
                stack.append(p)
            else:
                if not stack or p != paren_map[stack.pop()]:
                    return False

        return not stack
        