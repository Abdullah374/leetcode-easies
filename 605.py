from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n != 0:
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    i += 2
                    n -= 1
                else:
                    i += 1
        return n == 0