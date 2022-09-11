from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    count += 1

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        time = 0
        while q:
            coord = q.popleft()
            if coord[2] != time:
                time += 1

            for direction in directions:
                i = coord[0] + direction[0]
                j = coord[1] + direction[1]
                if i > -1 and i < n and j > -1 and j < m and grid[i][j] == 1:
                    count -= 1
                    grid[i][j] = 2
                    q.append((i,j,time + 1))

        return time if count == 0 else -1



        