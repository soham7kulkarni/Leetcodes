# We create dictionary/hashmap. We count the frequency of each element inside the dictionary. we start traversing the input using i and keep left pointer at 0. We take the length of the window and subtract the max frequency count. It represnts the number of replacements we have to make insie the window. If replacement exceeds k, we slide window by 1 to right. To do so, we decrement occurence of the element pointed by left by 1. We increment left pointer. When we increment i i.e the slidng window length we store inside res, which is our output for this program.

# TC: O(N), SC: O(26) = O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0

        for i in range(0, len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)

            while i-left+1 - max(count.values()) > k:
                count[s[left]] -= 1
                left+=1
            
            res = max(res, i-left+1)
        return res

        