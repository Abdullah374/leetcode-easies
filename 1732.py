from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxalt = 0
        current = 0

        for g in gain:
            current += g
            maxalt = max(maxalt, current)

        return maxalt