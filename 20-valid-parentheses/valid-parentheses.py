class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        toClose = {')':'(','}':'{',']':'['}
        for i in s:
            if i in toClose:
                if st and st[-1] == toClose[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False

        