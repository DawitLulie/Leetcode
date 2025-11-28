class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        result = []
        for i, val in enumerate(nums):
            if val > 0:
                result.append(i + 1)
        return result
