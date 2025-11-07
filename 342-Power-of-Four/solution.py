class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # Check power of two first
        if n & (n - 1) != 0:
            return False
        # Check that the single 1 bit is in the correct position for power of four
        return (n & 0x55555555) != 0
