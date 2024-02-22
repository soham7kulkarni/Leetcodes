class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s = set()
        mapp = {}
        for k in range(1, n+1):
            mapp[k] = 0
        for i,j in trust:
            s.add(i)
            mapp[j]+=1
        for l in mapp:
            if mapp[l] == n-1 and l not in s:
                return l
        return -1


        