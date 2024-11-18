class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1 = 0
        pt2 = 0
        merged = ''
        while pt1 < len(word1) and pt2 < len(word2):
            merged += word1[pt1]
            merged += word2[pt2]
            pt1 += 1
            pt2 += 1
        
        if pt1 < len(word1):
            merged = merged + word1[pt1:len(word1)]
        else:
            merged = merged + word2[pt2:len(word2)]
        return merged
