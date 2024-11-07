from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return None

        window_sum = sum(nums[:k])
        window_avg = window_sum/k
        max_avg = window_avg

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            window_avg = window_sum/k
            max_avg = max(max_avg,window_avg)
        return max_avg