class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        arr = d.most_common(k)
        result = [element for element,_ in arr]
        return result
        