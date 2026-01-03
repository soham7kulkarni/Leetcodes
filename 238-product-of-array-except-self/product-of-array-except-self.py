class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        running_product = 1
        for i in range(1,n):
            running_product = running_product*nums[i-1]
            answer[i] = running_product
        running_product = 1
        for i in range(n-2,-1,-1):
            running_product = running_product*nums[i+1]
            answer[i] = answer[i]*running_product
        return answer


        