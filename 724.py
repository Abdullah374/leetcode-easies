from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:len(nums)]):
        #         return i
        
        # if i == len(nums)-1:
        #     return -1
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            rightsum = total_sum - left_sum - nums[i]
            if rightsum == left_sum:
                return i 
            left_sum += nums[i]
        return -1