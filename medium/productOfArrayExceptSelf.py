from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                sum *= num
            else:
                zero_count += 1

        if zero_count >= 2:
            return [0]*len(nums)

        ans = []
        for num in nums:
            if zero_count == 0:
                ans.append(int(sum/num))
            else:
                ans.append(sum if num == 0 else 0)

        return ans


        # 3 cases that need to be considered


