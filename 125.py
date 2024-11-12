import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        
        charlist = list(s)

        i = 0
        j = len(charlist)-1
        while i<=j:
            if charlist[i] == charlist[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True