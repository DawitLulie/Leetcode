class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {name: i for i, name in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, name in enumerate(list2):
            if name in index_map:
                s = index_map[name] + j
                if s < min_sum:
                    min_sum = s
                    result = [name]
                elif s == min_sum:
                    result.append(name)
        return result
