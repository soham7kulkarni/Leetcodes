class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        temp = []
        for i in range(0, len(s)):
            #temp.append(s[i])
            char = s[i]
            if char in temp:
                index = temp.index(char)
                temp = temp[index + 1:]
                temp.append(char)
                maxLength = max(maxLength, len(temp))
            else:
                temp.append(char)
                maxLength = max(maxLength, len(temp))
            #print(temp)

        return maxLength