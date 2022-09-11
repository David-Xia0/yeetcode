from ast import Set
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set(nums)
        return len(mem) != len(nums)
        # time: O(N), mem: O(N)
        # can also sort to lower mem; time: O(NlogN), mem: O(1)