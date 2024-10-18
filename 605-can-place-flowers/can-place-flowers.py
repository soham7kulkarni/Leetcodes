class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the adjacent plots are also empty
                # Check left (i == 0 means no left neighbor)
                # Check right (i == length - 1 means no right neighbor)
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # Plant a flower
                    count += 1  # Increment the count of planted flowers
                    
                    # Early exit if we have planted enough flowers
                    if count >= n:
                        return True
        
        return count >= n  # Check if we planted at least n flowers