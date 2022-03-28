class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        start, end = 0, length-1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        