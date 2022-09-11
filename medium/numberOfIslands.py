from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(grid, r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]
                if new_r > -1 and new_r < n and new_c > -1 and new_c < m:
                    dfs(grid,  new_r, new_c )

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != "0":
                    count += 1
                    dfs(grid, i, j)
        
        return count

