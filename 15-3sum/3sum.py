class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arr = []

        for i in range(n-2):
            if nums[i] > 0:
                break

            low = i+1
            high = n-1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum == 0:
                    res =[nums[i], nums[low], nums[high]]
                    arr.append(res)
                    low += 1
                    high -= 1
                    while low < n-1 and nums[low] == nums[low-1]:
                        low += 1
                    while high >= 0 and nums[high] == nums[high+1]:
                        high -= 1
                elif sum > 0:
                    high -= 1
                else:
                    low += 1
        return arr    



