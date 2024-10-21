# Approach - taking 2 queue fo R and D
# We traverse thru main queue and store index of r and d respectively.
# We pop top elements from both queues and check who came first.
# We allow him to ban other party voter and then push him at the end for next round

# TC - O(N)
# SC - O(N)

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Create queues for both factions
        radiant = deque()
        dire = deque()

        # Fill the queues with the indices of the senators
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)  # Add index to radiant queue
            else:
                dire.append(i)  # Add index to dire queue
        
        # While both queues have senators
        while radiant and dire:
            # Get the indices of the next senators
            r_index = radiant.popleft()  # Radiant's senator index
            d_index = dire.popleft()      # Dire's senator index
            
            # Compare the indices to determine who votes first
            if r_index < d_index:
                # Radiant votes first and eliminates a Dire senator
                radiant.append(r_index + len(senate))  # Push back radiant's index to last for new round
            else:
                # Dire votes first and eliminates a Radiant senator
                dire.append(d_index + len(senate))  # Push back dire's index to last for new round
        
        # Determine the winner based on which queue is non-empty
        return "Radiant" if radiant else "Dire"
