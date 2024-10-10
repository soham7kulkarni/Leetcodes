# Naturally, we will start from the core to decode the string
# We are traversing to core through children of root so it is DFS
# Decode the string and then combine it with the root/parent

# Approach - DFS
# TC - O(N)
# SC - O(N)

class Solution:
    def decodeString(self, s: str) -> str:
        currString = ""
        currNum = 0
        charStack = []
        numStack = []
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                currNum = currNum*10 + int(ch)
            elif ch == '[':
                charStack.append(currString)
                numStack.append(currNum)
                currString = ""
                currNum = 0
            elif ch == ']':
                count = numStack.pop()
                child = count * currString
                parent = charStack.pop()
                currString = parent + child
            else:
                currString += ch
            i+=1
        return currString

        