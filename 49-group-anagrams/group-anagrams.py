# Approach - Instead of sorting each string (which takes O(Klog K)), this method uses a character count as a unique identifier for anagrams. We convert this list into a tuple (because lists are mutable and cannot be used as keys) and use it as a key in a defaultdict to group all strings that share that same frequency "signature".
# TC - O(N.K)
# SC - O(N.K)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
        