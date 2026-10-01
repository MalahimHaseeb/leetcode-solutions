class Solution:
    def removeStars(self, s: str) -> str:
        if not s:
            return ""
        
        stack = []

        for i in s:
            if i=="*":
                stack.pop()
                continue
            stack.append(i)
        
        return "".join(stack)
