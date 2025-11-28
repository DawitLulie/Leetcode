class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        stack = []

        for number in nums2:
            while stack and number > stack[-1]:
                smaller_number = stack.pop()
                next_greater_map[smaller_number] = number
            stack.append(number)
        
        for remaining_number in stack:
            next_greater_map[remaining_number] = -1

        result_list = [next_greater_map[number] for number in nums1]
        return result_list
