class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        if num is None or len(num) == 0: return result
        self.helper(num, 0, 0, 0, "", target,result)
        return result
    def helper(self, num: str, pivot: int, calc: int, tail: int, path: str, target: int, result: List[str]):
        # base
        if pivot == len(num):
            if calc == target:
                path = "".join(map(str, path))
                result.append(path)

        # logic
        for i in range(pivot, len(num)):
            if num[pivot] == "0" and i!= pivot: continue
            curr_str = num[pivot:i+1]
            curr = int(curr_str)
            
            if pivot == 0:
                self.helper(num, i + 1, curr, curr, curr_str, target, result)
            else:
                self.helper(num, i + 1, calc + curr, curr, path + "+" + curr_str, target, result)
                self.helper(num, i + 1, calc - curr, -curr, path + "-" + curr_str, target, result)
                self.helper(num, i + 1, calc - tail + tail * curr, tail * curr, path + "*" + curr_str, target, result)
