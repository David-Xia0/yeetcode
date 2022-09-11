from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            else:
                mid = left + 1
                right =  len(nums) - 1
                while mid < right:
                    sum = nums[left] + nums[mid] + nums[right]
                    if sum == 0:
                        ans.append([nums[left], nums[mid], nums[right]])
                        mid += 1
                        while mid < right and nums[mid] == nums[mid - 1]:
                            mid += 1
                        right -= 1
                        while mid < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum < 0:
                        mid += 1
                    elif sum > 0:
                        right -=1
        return ans
                
        # Can use 3 pointers. First pointer goes right, while last two pointers converge interval
        # Another approach is to create lists of negative and postive numbers, the divide and conquer the problem space