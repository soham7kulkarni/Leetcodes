class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count, s2count = [0] * 26, [0] * 26

        # Count the frequencies of characters in the first window of s2
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        # Use a sliding window to compare character frequencies
        for r in range(len(s1), len(s2)):
            if s1count == s2count:
                return True

            # Update the window by removing the leftmost character and adding the rightmost character
            s2count[ord(s2[r]) - ord('a')] += 1
            s2count[ord(s2[r - len(s1)]) - ord('a')] -= 1

        # Check the last window
        if s1count == s2count:
            return True

        return False




