class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:   # Current left-asteroid is larger
                    stack.pop()     # Right asteroid explodes
                    continue        # Check previous stack top
                elif stack[-1] == -a:
                    stack.pop()     # Both explode
                    break
                else:
                    break           # Left asteroid explodes

            else:
                stack.append(a)     # No collision or after handling

        return stack

                