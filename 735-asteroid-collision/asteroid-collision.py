# Its important to consider the exactly all cases and determine when collision will occur and it wont
# In this case, if positive asteroid is the next one, there will never be a collision
# Also, stack can have mix of positive and negative asteroids. 
# Assumption: stack will have only positives or negatives is wrong

# TC - O(2N) = O(N)
# Although we have nested while inside for loop, we push or pop each asteroid max once. 
# So in case [5,10,-15,-20], when -20 is anticipated, only -15 is present in stack
# Hence assuming traversing over all elements of stack will result in O(N) is not necessarily true 
# And stack operations which dominate the while loop are of linear complexity 


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

                    


        