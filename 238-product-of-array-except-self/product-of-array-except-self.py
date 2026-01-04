class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        rp = 1
        for i in range(1, n):
            rp = rp * nums[i-1]
            answer[i] = rp
        rp = 1
        for i in range(n-2, -1, -1):
            rp = rp * nums[i+1]
            answer[i] = answer[i] * rp
        return answer
        