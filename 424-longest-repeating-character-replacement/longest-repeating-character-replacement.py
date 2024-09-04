class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        maxLength = 0
        left = 0
        for i in range(0, len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)

            while i - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left+=1
            maxLength = max(maxLength, (i - left + 1))
        return maxLength

                


        