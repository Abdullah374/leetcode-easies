from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for number in arr:
            if number not in hashmap:
                hashmap[number] = 1
            else:
                hashmap[number] += 1
        prev = None
        
        values = hashmap.values()
        return len(values) == len(set(values))