class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = 1
        n = len(nums)
        answer = [0] * n
        answer[0] = 1
        for i in range(1,len(nums)):
            pr = pr * nums[i-1]
            answer[i] = pr
        pr = 1
        for i in range(n-2,-1,-1):
            pr = pr * nums[i+1]
            answer[i] = answer[i] * pr
        return answer
            

        