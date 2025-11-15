class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
