from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        new_digits = digits[::-1]
        for i in range(len(new_digits)):
            number += new_digits[i] * pow(10, i)
        number += 1
        answer = str(number)
        digits = []
        for letter in answer:
            x = int(letter)
            digits.append(x)
        return digits
