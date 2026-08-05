class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        st = []
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                popped = st.pop()
                answer[popped] = i - popped
            st.append(i)
        return answer
        