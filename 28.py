class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            x = haystack.index(needle)
            return x
        else:
            return -1

         
        
