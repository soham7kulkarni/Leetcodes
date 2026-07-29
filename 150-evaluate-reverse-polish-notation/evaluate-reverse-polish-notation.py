class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        total = 0
        for i in tokens:
            if i == "+":
                total = st.pop() + st.pop()
                st.append(total)
            elif i == "-":
                b, a = st.pop(), st.pop()
                total = a - b
                st.append(total)
            elif i == "*":
                total = st.pop()*st.pop()
                st.append(total)
            elif i == "/":
                b, a = st.pop(), st.pop()
                total = int(a/b)
                st.append(total)
            else :
                st.append(int(i))
        return st[-1] 
        