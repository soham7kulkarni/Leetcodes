from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes):
        ans = []
        szToGroup = defaultdict(list)

        for i, size in enumerate(groupSizes):
            szToGroup[size].append(i)

            # When the list size equals the group size, store it in the answer and reset.
            if len(szToGroup[size]) == size:
                ans.append(szToGroup[size])
                szToGroup[size] = []

        return ans
