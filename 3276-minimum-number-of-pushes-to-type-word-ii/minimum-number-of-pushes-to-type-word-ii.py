class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = [0] * 26
        for c in word:
            arr[ord(c) - ord('a')] += 1

        sorted_arr = sorted(arr, reverse = True)
        totalpresses = 0
        multiplier = 1
        for i in range(26):
            if sorted_arr[i] == 0:
                break
            if i % 8 == 0 and i != 0:
                multiplier += 1
            totalpresses += sorted_arr[i] * multiplier
        return totalpresses

        