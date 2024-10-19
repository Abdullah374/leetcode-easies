from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array = []
        for num in nums:
            num = num **2
            array.append(num)

        array = sorted(array)
        return array
