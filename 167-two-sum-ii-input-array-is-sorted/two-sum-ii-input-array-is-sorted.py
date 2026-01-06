# Approach 1 - checking combination of each element with every other element in array. O(N*N)
# Approach 2 - Two Pointers. take sum. increase or decrease left or right pointers aacording to sum.
# TC - O(N), SC - O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        ans = []
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                ans.append(p1+1)
                ans.append(p2+1)
                break 
            while numbers[p1] + numbers[p2] < target:
                p1 += 1
            while numbers[p1] + numbers[p2] > target:
                p2 -= 1
        return ans
            
        