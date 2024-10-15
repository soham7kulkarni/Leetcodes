# TC - O(N), SC - O(1)
# Creating dictionary and checking the match of closing characters 
# with their opening character
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in closeToOpen:
                if st and st[-1] == closeToOpen[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False

        