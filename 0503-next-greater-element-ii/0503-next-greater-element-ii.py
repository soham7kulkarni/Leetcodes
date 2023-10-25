# Used the same approach which we used for daily temperature/warmer day problem. but here,we traverse through the array twice and find the FIRST maximum, since it is a circular array, mwe might find greater element behidn the current element.
# TC - O(2N = N), SC - O(N)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        st = []
        n = len(nums)
        for i in range(2*n):
            while st and nums[i%n] > nums[st[-1]]:
                popped = st.pop()
                res[popped] = nums[i%n]
            if i < n:
                st.append(i)
        return res

        