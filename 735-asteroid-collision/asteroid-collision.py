class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while st and i < 0 and st[-1] > 0:
                top = st.pop()
                if top + i == 0:
                    break
                elif top + i > 0:
                    st.append(top)
                    break
            else:
                st.append(i)
        return st

                    


        