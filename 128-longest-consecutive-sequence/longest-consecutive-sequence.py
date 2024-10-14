# Brute Force - sort the numbers and traverse to check longest sequence
# TC - O(nlogn)

# Optimal - Put elements in the set
# for each number, check if i-1 exists
# if yes, already part of sequence, skip (we skip 4 when 1,2,3 are present)
# if no, reset count and longest to 1(we start processing 1 and increment)
# start finding next elements
# updating longest using count variable

# TC - O(N), exact 2N, 
# suppose we find 1 at last
# then we have already traversed array omce and we will go theough array
# once again to find sequence for last element(1)
# SC - O(N)


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
                while x + 1 in arr:
                    count += 1
                    x += 1
                    longest = max(count, longest)
        return longest
        