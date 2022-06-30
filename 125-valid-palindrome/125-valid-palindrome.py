class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        size = len(s)
        i, j = 0, size-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
                continue
            while i < j and not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        