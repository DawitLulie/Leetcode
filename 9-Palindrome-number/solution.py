class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        original = num
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        return original == reversed_num
