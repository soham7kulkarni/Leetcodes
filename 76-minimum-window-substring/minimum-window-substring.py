# TC - O(m + n)
# SC - O(1)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Count the frequency of characters in t
        dict_t = Counter(t)
        required = len(dict_t)

        # Two pointers and some data structures
        l, r = 0, 0  # Left and right pointers
        formed = 0  # To keep track of how many unique characters in t are present in the current window
        window_counts = defaultdict(int)  # Count of characters in the current window
        min_len = float('inf')  # Initialize min length of the window
        min_window = (0, 0)  # Start and end index of the minimum window

        while r < len(s):
            char = s[r]  # Add character from the right pointer
            window_counts[char] += 1  # Update count in the current window

            # Check if the current character's count matches the required count
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1  # If it matches, increment formed

            # Try and contract the window until it's no longer valid
            while l <= r and formed == required:
                char = s[l]  # Character to be removed from the window

                # Save the smallest window and its length
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)

                # Remove the character from the left pointer
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1  # If it drops below the required count, decrement formed

                l += 1  # Move left pointer to the right

            r += 1  # Move right pointer to the right

        # Return the smallest window or empty string if no valid window exists
        return "" if min_len == float('inf') else s[min_window[0]: min_window[1] + 1]
        