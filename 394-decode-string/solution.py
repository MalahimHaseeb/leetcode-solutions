class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        
        stack = []
        current = []
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((current, num))
                current = []
                num = 0
            elif char == ']':
                prev, k = stack.pop()
                prev.append("".join(current) * k)
                current = prev
            else:
                current.append(char)
            
        return "".join(current)
