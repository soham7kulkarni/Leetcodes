class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxCount = 0
        maxLength = 0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1
            maxCount = max(maxCount, count[s[right]])

            if (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right-left+1)
        return maxLength 
        