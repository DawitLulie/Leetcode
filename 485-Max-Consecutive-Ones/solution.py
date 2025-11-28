class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_streak = 0
        current_streak = 0
        
        for value in nums:
            if value == 1:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 0
        
        return longest_streak
