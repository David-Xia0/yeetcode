from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, visited):
            arr = []
            for n in nums:
                if n in visited:
                    continue
                visited.add(n)
                arr.extend([perm + [n]  for perm in dfs(nums, visited)])
                visited.remove(n)
            return arr if arr else [[]]
        return dfs(nums, set())