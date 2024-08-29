class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = 0
        element = None
        for n in nums:
            if frequency == 0:
                frequency += 1
                element = n
            else:
                if n == element:
                    frequency += 1
                else:
                    frequency -= 1
        return element
        

        