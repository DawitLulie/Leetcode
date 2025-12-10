class Solution:
    def findLHS(self, nums):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        best = 0
        for key in freq:
            if key + 1 in freq:
                best = max(best, freq[key] + freq[key + 1])
        
        return best
    