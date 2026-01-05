class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        longest = 1
        arr = set(nums)
        for i in arr:
            if i-1 not in arr:
                count = 1
                x = i
                while x+1 in arr:
                    count += 1
                    x += 1
                    longest = max(longest, count)
        return longest
        