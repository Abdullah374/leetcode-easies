class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        left = 0
        right = 0

        while right < len(t):
            if t[right] == s[left]:
                left += 1
                if left == len(s):
                    return True
            right += 1
        return left == len(s)

        