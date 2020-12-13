class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        paren_map = {')': '(', ']': '[', '}': '{'}
        for string in s:
            if string not in paren_map:
                stack.append(string)
            elif not stack or paren_map[string] != stack.pop(-1):
                return False
        return not stack