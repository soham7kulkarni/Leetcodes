# Approach - DFS
# TC - O(N)
# SC - O(N)

class Solution:
    def decodeString(self, s: str) -> str:
        str_st = []
        num_st = []
        curr_str = ""
        curr_num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                curr_num = curr_num *10 + int(c)
            elif c == '[':
                str_st.append(curr_str)
                num_st.append(curr_num)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                count = num_st.pop()
                child = curr_str * count
                parent = str_st.pop()
                curr_str = parent + child
            else:
                curr_str += c
            i+=1
        return curr_str

        