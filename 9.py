class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        n = len(a)

        pal = True
        for i in range(n):
            j = n-1
            if a[i] != a[j]:
                pal = False
            else:
                n = n-1
        return pal
