class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, result = 0, 0
        size = len(s)
        charMap = dict()
        max_freq = 0
        for right in range(size):
            char = s[right]
            charMap[char] = charMap.get(char, 0) + 1
            max_freq = max(max_freq, charMap.get(char))
            if (right - left + 1) - max_freq > k:
                charMap[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result