from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            pos = nums.index(target)
            return pos
        else:
            c_pos = 0
            for number in nums:
                if target > number:
                    c_pos = nums.index(number) + 1
            return c_pos 
        
