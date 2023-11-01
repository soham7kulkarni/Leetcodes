class TimeMap:
# TC - O(1)
    def __init__(self):
        self.store = {}

# TC - O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
# TC - O(logn)
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l = 0
        r = len(values)-1
        while l<=r:
            mid = l + (r-l)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)