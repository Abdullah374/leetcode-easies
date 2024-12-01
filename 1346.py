from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for number in arr:
            if number == 0:
                arr.remove(number)
            double = 2 * number
            if double in arr:
                return True
        return False