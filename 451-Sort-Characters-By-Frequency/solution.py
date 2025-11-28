class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_map = {}
        for character in s:
            frequency_map[character] = frequency_map.get(character, 0) + 1

        characters_sorted_by_frequency = sorted(
            frequency_map.keys(), 
            key=lambda character: frequency_map[character], 
            reverse=True
        )

        result_string = []
        for character in characters_sorted_by_frequency:
            result_string.append(character * frequency_map[character])

        return "".join(result_string)
