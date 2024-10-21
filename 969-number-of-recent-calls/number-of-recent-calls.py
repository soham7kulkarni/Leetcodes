# Approach - we can have stack and can maintain number of ping requests alongside time value
# but here, we are not taking care of old calls. Hence we will simply discard them using queue

# TC - O(N)
# SC - O(N)

from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize the queue to store the timestamps of requests
        self.requests = deque()
    
    def ping(self, t: int) -> int:
        # Append the new request time
        self.requests.append(t)
        
        # Remove requests that are older than t - 3000
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()  # Remove the oldest request
            
        # Return the number of requests in the last 3000 ms
        return len(self.requests)        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)