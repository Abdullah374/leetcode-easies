from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            key = i
            if key in nums:
                continue
            else:
                break
        return key
            

            