class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for val in asteroids:

            should_keep = True

            while should_keep and stack and stack[-1] > 0 and val < 0:
                top = stack[-1]

                if top == -val:
                    stack.pop()
                    should_keep = False
                elif top > -val:
                    should_keep = False
                else:
                    stack.pop()
            
            if should_keep:
                stack.append(val)

        return stack
