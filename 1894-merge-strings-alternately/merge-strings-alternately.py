class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        result = ""
        if not m and not n:
            return result
        minimum = min(m,n)
        for i in range(minimum):
            result += word1[i]
            result += word2[i]
        if m > n:
            result += word1[i+1:]
        else:
            result += word2[i+1:]
        return result

        