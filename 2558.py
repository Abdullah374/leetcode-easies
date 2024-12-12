import heapq
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        total = sum(gifts)

        for _ in range(k):
            largest_gift = -heapq.heappop(max_heap)
            new_value = int(largest_gift ** 0.5)
            total -= (largest_gift - new_value)
            heapq.heappush(max_heap, -new_value)
            
        return total
