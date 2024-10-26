from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        base = len(nums)//2
        number_count = Counter(nums)
        for number, count in number_count.items():
            if count>base:
                return number

        