from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mem = {}
        halflength = len(nums)//2

        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1

            if mem[num] > halflength:
                return num
            
# solve for memory: O(1) by only requiring one count, the majority element will always survive a free for all