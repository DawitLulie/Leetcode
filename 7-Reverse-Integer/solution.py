class Solution:
    def reverse(self, number: int) -> int:
        sign = -1 if number < 0 else 1
        reversed_number = int(str(abs(number))[::-1]) * sign

        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0

        return reversed_number
