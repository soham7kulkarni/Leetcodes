class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == "+":
                st.append(st.pop()+st.pop())
            elif c == "-":
                b,a = st.pop(), st.pop()
                st.append(a-b)
            elif c == "*":
                st.append(st.pop()*st.pop())
            elif c == "/":
                b,a = st.pop(), st.pop()
                st.append(int(a/b))
            else:
                st.append(int(c))
        return st[0]