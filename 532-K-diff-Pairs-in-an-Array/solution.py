class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        seen = set()
        duplicates = set()
        for num in nums:
            if k == 0:
                if num in seen:
                    duplicates.add(num)
            else:
                if num + k in seen:
                    duplicates.add(num)
            seen.add(num)
        return len(duplicates)
