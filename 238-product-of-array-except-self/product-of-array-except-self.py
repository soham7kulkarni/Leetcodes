# Approach 1 - two nested for loops and then when i == j, 
# we will not do multiplication or else do multiplication. TC - O(N*N)
# Approach 2 - multiplication of all elements to the left of that element 
# in first for loop and 
# all right in second pass. Multiply them with the resultant itself to save on space. 
# Or else two result array and multiply them. 
# O(N), O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        running_product = 1
        answer[0] = 1
        for i in range(1, n):
            running_product = running_product * nums[i-1]
            answer[i] = running_product
        answer[n-1] = running_product
        running_product = 1
        for i in range(n-2, -1, -1):
            running_product = running_product*nums[i+1]
            answer[i] = answer[i]*running_product
        return answer



