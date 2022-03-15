class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        longest = 1
        start, end = 0, 0
        hm = {s[start]:start}
        while end < length-1:
            end = end + 1
            char = s[end]
            if (char in hm) and (hm[char] >= start):
                start = hm[char]+1
            hm[char] = end
            current_length = end-start+1
            if current_length > longest:
                longest = current_length
        return longest
        