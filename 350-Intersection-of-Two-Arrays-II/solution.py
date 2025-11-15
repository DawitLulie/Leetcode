from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for n in nums1:
            count[n] = count.get(n, 0) + 1

        result = []
        for n in nums2:
            if n in count and count[n] > 0:
                result.append(n)
                count[n] -= 1

        return result
