class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(n):
            
            result = 0
            while n > 0:
                digit = n % 10
                result += digit**2
                n = n//10
                
            return result

        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = calc(n)
        return True
        
