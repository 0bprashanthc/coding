class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        size = len(s2)
        window_size = len(s1)
        if window_size > size:
            return False
        left, right = 0, window_size-1
        while right < size:
            substring = s2[left:right+1]
            if self.valid_anagram(s1, substring):
                return True
            left += 1
            right += 1
        return False
        """
        size = len(s2)
        window_size = len(s1)
        if window_size > size: return False
        s1_count, s2_count = [0]*26, [0]*26
        for i in range(window_size):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)
        left = 0
        for i in range(window_size, size):
            if matches == 26: return True
            char = s2[i]
            index = ord(char)-ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] == s2_count[index]-1:
                matches -= 1
            
            char = s2[left]
            index = ord(char)-ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] == s2_count[index]+1:
                matches -= 1
            left += 1
        return matches == 26
    
    def valid_anagram(self, s1, s2):
        _map = dict()
        size = len(s1)
        if size != len(s2):
            return False
        for i in range(size):
            _map[s1[i]] = _map.get(s1[i],0)+1
            _map[s2[i]] = _map.get(s2[i],0)-1
        for freq in _map.values():
            if freq != 0:
                return False
        return True