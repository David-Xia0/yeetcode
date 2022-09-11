from http.client import ImproperConnectionState
from typing import List
import math
import heapq

class Solution:
    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: math.dist([0,0], x))
        return points[:k]


    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for p in points:
            if len(distance) < k:
                heapq.heappush(distance, (-(p[0]**2 + p[1]**2),p))
            else:
                heapq.heappush(distance, (-(p[0]**2 + p[1]**2),p))
                heapq.heappop(distance)
               
        return [i[1] for i in distance]


