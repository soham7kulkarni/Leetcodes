# Approach BFS - Remove 1 parenthesis at a time and 
# abondon the children (posiible combination without it) inside queue.
# Check if we get possible output and 
# keep on removing 1 parenthesis till we get possible answers

# Approahc DFS - Remove 1 parenthesis at a time and maintain possible outcomes and 
# max length. If we get bigger outcome we replace or keep it alongside the other outcomes.
# We maintain hashsets to avoid processing the same sequence.

# TC - O(N^N) SC - O(N^N)
class Solution:
    def __init__(self):
        self.max = 0 # max length of the valid substring
        self.result = [] #to hold the output
        self.set = set() # for not repating the already processed subsequence
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        self.dfs(s)
        return self.result

    def dfs(self, s):
        if len(s) < self.max: return #If we have output len = 5 why check substring of 4 characters
        if self.isValid(s):
            if len(s) > self.max:
                self.result = [] #Discarding previous short subsequence
                self.max = len(s)
            self.result.append(s) #Adding it to output

        # logic
        for i in range(len(s)):
            c = s[i]
            if c != '(' and c != ')': continue #if its character continue
            child = s[:i] + s[i+1:] #subsequence without that particular char
            if child not in self.set: #If child not present in set then only add
            # and process or else just skip that child
                self.set.add(child)
                self.dfs(child) 

    def isValid(self, s) -> bool:
        count = 0
        for i in range(len(s)):
            c = s[i]
            if c != '(' and c != ')': continue #if its character continue
            elif c == '(': count+=1
            else:
                if count == 0: return False
                count-=1
        return count == 0




        