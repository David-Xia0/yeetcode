from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            if nums[i] in mem:
                return[i, mem[nums[i]]]
            else:
                mem[target - nums[i]] = i
        