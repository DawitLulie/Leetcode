class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        seen = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            rem = total % k

            if rem in seen:
                if i - seen[rem] > 1:
                    return True
            else:
                seen[rem] = i

        return False
