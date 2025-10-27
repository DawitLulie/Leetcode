class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        if needle_length > haystack_length:
            return -1
        
        for start_index in range(haystack_length - needle_length + 1):
            substring = haystack[start_index:start_index + needle_length]
            if substring == needle:
                return start_index
        
        return -1
