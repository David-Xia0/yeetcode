from heapq import merge
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for index, i in enumerate(intervals):
            if i[1] < newInterval[0]:
                res.append(i)
            elif newInterval[1] < i[0]:
                res.append(newInterval)
                return res+intervals[index:]  # can return earlier
            else:  # overlap case
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        res.append(newInterval)
        return res
