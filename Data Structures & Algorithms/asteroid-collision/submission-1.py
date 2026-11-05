class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in range(len(asteroids)):
            cand=True
            while stack and asteroids [i] < 0 and stack[-1] > 0:
                if stack[-1] > abs(asteroids [i]):
                    cand=False
                    break
                elif stack[-1] < abs(asteroids [i]):
                    stack.pop()
                
                elif stack[-1] == abs(asteroids [i]):
                    stack.pop()
                    cand=False
                    break

            if cand :
                stack.append(asteroids [i])

            
        return stack

