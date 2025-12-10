class Solution:
    def distributeCandies(self, candyType):
        unique = len(set(candyType))
        limit = len(candyType) // 2
        return min(unique, limit)
