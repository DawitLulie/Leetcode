class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in used:
                return [used[diff], index]
            used[number] = index