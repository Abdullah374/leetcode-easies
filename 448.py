from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        v = [-1] * (n+1)
        v[0] = 1
        result = []
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] ==-1:
                result.append(i)
        return result
