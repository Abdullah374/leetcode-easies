from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum = max(candies)

        for candy in candies:
            if (candy + extraCandies) >= maximum:
                result.append(True)
            else:
                result.append(False)

        return result