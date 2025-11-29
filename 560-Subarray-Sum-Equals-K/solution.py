class Solution:
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        sums = {0: 1}

        for num in nums:
            total += num
            if total - k in sums:
                count += sums[total - k]
            sums[total] = sums.get(total, 0) + 1

        return count
