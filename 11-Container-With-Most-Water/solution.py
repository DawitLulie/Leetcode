class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_water = min(heights[left], heights[right]) * width
            max_water = max(max_water, current_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
