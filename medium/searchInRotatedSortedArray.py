from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        c = float('-inf') if target < nums[0] else float('inf')
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            num = nums[mid] if (nums[mid] < nums[0]) == (target < nums[0]) else c
            if num > target:
                right = mid - 1
            elif num < target:
                left = mid + 1
            else:
                return mid
        return -1

