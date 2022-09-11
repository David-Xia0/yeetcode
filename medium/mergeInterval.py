from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for i in intervals:
            if not ans or i[0] > ans[-1][1]: # overlapping
                ans.append(i)
            else:
                ans[-1][1] = max(i[1],ans[-1][1])
        return ans
