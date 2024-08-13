class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime, reverse = True)
        tasks = sorted(tasks)
        cp = 0
        result = 0
        for i in range(3, len(tasks), 4):
            print(i)
            maximum = processorTime[cp] + tasks[i]
            cp += 1
            result = max(maximum, result)

        return result



        