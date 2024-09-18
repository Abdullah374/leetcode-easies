class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = s.split()
        length = len(y[-1])
        return length