from distutils.dep_util import newer_group
from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        ans = [ [0]*m for i in range(n) ]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    ans[i][j] = -1
        
        while len(q) != 0:
            pos = q.popleft()

            for direction in directions:
                new_r = pos[0] + direction[0]
                new_c = pos[1] + direction[1]
                if new_r != n and new_c != m and new_r != -1 and new_c != -1:    
                    if ans[new_r][new_c] == -1:
                        ans[new_r][new_c] = ans[pos[0]][pos[1]] + 1
                        q.append((new_r, new_c))
        
        return ans

        