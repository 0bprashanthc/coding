class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _map = dict()
        size = len(s)
        for i in range(size):
            _map[s[i]] = _map.get(s[i],0)+1
            _map[t[i]] = _map.get(t[i],0)-1
        for _, count in _map.items():
            if count != 0:
                return False
        return True
            
        