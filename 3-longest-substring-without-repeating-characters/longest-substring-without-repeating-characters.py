class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        left = 0
        right = 0
        res = 0
        while right < len(s):
            c = s[right]
            counter[c] += 1
            while counter[c] > 1:
                l = s[left]
                counter[l] -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res


        