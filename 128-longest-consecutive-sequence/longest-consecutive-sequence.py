class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = set(nums)
        long_str = 1
        for i in arr:
            if i-1 not in arr:
                cur_str = 1
                length = 1
                while i + length in arr:
                    cur_str += 1
                    length += 1
                    long_str = max(long_str, cur_str)
        return long_str

        