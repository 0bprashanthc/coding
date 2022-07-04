class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        left, right = 0, 0
        chars = [0] * 128
        result = 0
        while right < size:
            char = s[right]
            chars[ord(char)] += 1
            while chars[ord(char)] > 1:
                chars[ord(s[left])] -= 1
                left += 1
            result = max(result, right-left+1)
            right += 1
        return result